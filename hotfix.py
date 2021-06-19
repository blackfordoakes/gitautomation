from git import Repo

def hotfix():
    # get the cirrent GIT directory
    repo = Repo()
    assert not repo.bare
    
    # get the current tag
    print ("Current tags:")
    tags = repo.tags
    for tag in tags:
        print (tag)
    
    # ask user for tag
    tag_to_find = input("Please select the tag to branch from: ")
    tag_to_find = tag_to_find.lower().strip()

    if not tag_to_find:
        print ("No tag entered.")
        return
    elif tag_to_find == "qa":
        print ("QA is not a valid selection.")
        return;

    hotfix_tag = None
    for x in tags:
        if x.name == tag_to_find:
            hotfix_tag = x
            break

    if not hotfix_tag:
        print ("Invalid tag to branch from.")
        return
    
    print ("Branching from " + tag_to_find)
    new_branch = repo.create_head("hotfix_" + tag_to_find)
    print ("Setting branch to commit " + str(hotfix_tag.commit))
    new_branch.set_commit(hotfix_tag.commit)
    print ("Pushing to remote...")
    repo.git.push('--set-upstream', 'origin', new_branch)

if __name__ == "__main__":
    hotfix();