from git import Repo

def prepare_release():
    # get the current GIT directory
    repo = Repo()
    assert not repo.bare
    
    # suggest a tag
    suggested_tag = suggest_version(repo.tags)
    
    # ask user for new tag
    new_tag = input("Please enter the version number (ENTER for " + suggested_tag + "): ")
    new_tag = new_tag.lower().strip()

    if not new_tag:
        new_tag = suggested_tag

    created_tag = find_tag(new_tag, repo.tags)
    if created_tag:
        print("Tag already exists")
        return
    
    print ("Tagging current revision with: " + new_tag)
    created_tag = repo.create_tag(new_tag)
    repo.remotes.origin.push(created_tag)

    # if the QA tag exists, move it
    qa_tag = find_tag("qa", repo.tags)
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

def suggest_version(tagList):
    suggestion = "0.0.1"
    try:
        last = tagList[-1]
        suggestion = last.name

        if suggestion == "qa":
            last = tagList[-2]
            suggestion = last.name
        
        print("Latest tag is: " + suggestion)
        parts = suggestion.split(".")
        incremented = int(parts[-1]) + 1
        parts[-1] = str(incremented)
        suggestion = ".".join(parts)
    except:
       suggestion = "0.0.1"

    return suggestion

if __name__ == "__main__":
    prepare_release()