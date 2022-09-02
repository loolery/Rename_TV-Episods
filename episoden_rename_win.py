import os, sys, re
from typing import List

def main():
    if len(sys.argv) > 4:
        print("Zuviele Parameter!")
        sys.exit()
    elif len(sys.argv) == 2:
        section = '#SERiEN'
    elif len(sys.argv) == 3:
        section = str(sys.argv[2])
    elif len(sys.argv) == 4:
        section = str(sys.argv[2])
        option = int(sys.argv[3])
    elif len(sys.argv) == 1:
        print("""\n        min 1 Parameter muss angegeben werden!
        ---------------------------------------
    Parameter1:     Releasename
    Parameter2(optional):   Sectionname (default: #SERiEN)
    Parameter3(optional):   1 = Ordner erst erstellen
    \n""")
        sys.exit()
    releasename = str(sys.argv[1])
    standartdir = 'J:\\zrelease.german.sogehts.x264-haha'
    print(section)
    workdir = standartdir + '\\' + section + '\\' + releasename
    if option == 1:
        CreateFolder(workdir)
    # if os.path.exists(workdir):
        # staffeln = os.listdir(workdir)
        # staffeln.sort()
        # for staffel in staffeln:
            # episoden = os.listdir(workdir + '\\' + staffel)
            # episoden.sort()
            # episodennr = 1
            # for episode in episoden:
                # dateien = os.listdir(workdir + '\\' + staffel + '\\' + episode)
                # dateien.sort()
                # for datei in dateien:
                    # filesplit = re.split('^[\S]*[Ee]{1}[\d]{2,3}', datei)
                    # neuerdateiname = releasename.lower() + '-' + staffel.lower() + 'e' + str(episodennr).zfill(2) + filesplit[1]
                    # os.rename(workdir + '\\' + staffel + '\\' + episode + '\\' + datei, workdir + '\\' + staffel + '\\' + episode + '\\' + neuerdateiname)
                    # print("    - " + datei + r"    --->  " + neuerdateiname)
                # foldersplit = re.split('^[\S]*[Ee]{1}[\d]{2,3}', episode)
                # print(workdir + '\\' + staffel + '\\' + episode + ' ---> ' + releasename + '.' + staffel + 'E' + str(episodennr).zfill(2) + foldersplit[1])
                # os.rename(workdir + '\\' + staffel + '\\' + episode, workdir + '\\' + staffel + '\\' + releasename + '.' + staffel + 'E' + str(episodennr).zfill(2) + foldersplit[1])
                # episodennr +=1
    # else:
        # print("Pfad existiert nicht! " + workdir)
        
def CreateFolder(cf_workdir):
    if os.path.exists(cf_workdir):
        cf_staffeln = os.listdir(cf_workdir)
        cf_staffeln.sort()
        for cf_staffel in cf_staffeln:
            cf_dateien = os.listdir(cf_workdir + '\\' + cf_staffel)
            cf_dateien.sort()
            for cf_datei in cf_dateien:
                cf_ordnername = re.split('.[a-z]{3}$', cf_datei)
                print(cf_ordnername[0])
                os.mkdir(cf_workdir + '\\' + str(cf_staffel) + '\\' + cf_ordnername[0])
                os.replace(cf_workdir + '\\' + str(cf_staffel) + '\\' + cf_datei, cf_workdir + '\\' + str(cf_staffel) + '\\' + cf_ordnername[0] + '\\')
            episodennr +=1
            
if __name__ == '__main__':
    main()
