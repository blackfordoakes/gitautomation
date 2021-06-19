from git import Repo
import os.path

class GitReleaser:
    def __init__(self):
        self.rorepo = Repo()

    def main(self):
        # get the cirrent GIT directory
        repo = Repo(self.rorepo.working_tree_dir)
        assert not repo.bare
        
        # get the current tag
        print ("current tags:")
        tags = repo.tags
        for tag in tags:
            print (tag)
        
        # ask user for new tag
        new_tag = input("Please enter the version number: ")
        new_tag = new_tag.lower().strip()

        if not new_tag:
            print ("No version entered.")
            return
        
        print ("Tagging current revision with: " + new_tag)
        repo.create_tag(new_tag)

        # if the QA tag exists, move it
        qa_tag = None
        for x in tags:
            if x.name == "qa":
                qa_tag = x
                break

        if qa_tag:
            print("moving the qa tag")
            repo.delete_tag(qa_tag)

        repo.create_tag("qa")

if __name__ == "__main__":
    objName = GitReleaser()
    objName.main() 