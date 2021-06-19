from git import Repo

def prepare_release():
    # get the current GIT directory
    repo = Repo()
    assert not repo.bare
    
    # get the current tag
    print ("Current tags:")
    tags = repo.tags
    for tag in tags:
        print (tag)
    
    # ask user for new tag
    new_tag = input("Please enter the version number: ")
    new_tag = new_tag.lower().strip()

    if not new_tag:
        print ("No version entered.")
        return

    created_tag = find_tag(new_tag, tags)
    if created_tag:
        print("Tag already exists")
        return
    
    print ("Tagging current revision with: " + new_tag)
    created_tag = repo.create_tag(new_tag)
    repo.remotes.origin.push(created_tag)

    # if the QA tag exists, move it
    qa_tag = find_tag("qa", tags)
    if qa_tag:
        print("Moving the qa tag")
        repo.delete_tag(qa_tag) # remove local
        repo.remotes.origin.push(refspec=(':%s' % (qa_tag))) # remove remote

    qa_tag = repo.create_tag("qa")
    repo.remotes.origin.push(qa_tag)

def find_tag(tag_name, taglist):
    found_tag = None
    for x in taglist:
        if x.name == tag_name:
            found_tag = x
            break
    
    return found_tag

if __name__ == "__main__":
    prepare_release()