import os, sys, re
from typing import List

def main():
    section = '#SERiEN'
    option = 0
    if len(sys.argv) > 4:
        print("Zuviele Parameter!")
        sys.exit()
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
    standartdir = r'/home/glftpd/site'
    workdir = standartdir + '/' + section + '/' + releasename
    if option == 1:
        CreateFolder(workdir)
    if os.path.exists(workdir):
        staffeln = os.listdir(workdir)
        staffeln.sort()
        for staffel in staffeln:
            episoden = os.listdir(workdir + '/' + staffel)
            episoden.sort()
            episodennr = 1
            for episode in episoden:
                dateien = os.listdir(workdir + '/' + staffel + '/' + episode)
                dateien.sort()
                for datei in dateien:
                    filesplit = re.split('^[\S]*[Ee]{1}[\d]{2,3}', datei)
                    neuerdateiname = releasename.lower() + '-' + staffel.lower() + 'e' + str(episodennr).zfill(2) + filesplit[1]
                    os.rename(workdir + '/' + staffel + '/' + episode + '/' + datei, workdir + '/' + staffel + '/' + episode + '/' + neuerdateiname)
                    if os.path.exists(workdir + '/' + staffel + '/' + episode + '/' + neuerdateiname):
                        print(" Rename file " + datei + r"   --->  " + neuerdateiname + ' OK')
                    else:
                        print(" Rename file " + datei + r"   --->  " + neuerdateiname + ' FAiLED')
                foldersplit = re.split('^[\S]*[Ee]{1}[\d]{2,3}', episode)
                os.rename(workdir + '/' + staffel + '/' + episode, workdir + '/' + staffel + '/' + releasename + '.' + staffel + 'E' + str(episodennr).zfill(2) + foldersplit[1])
                if os.path.exists(workdir + '/' + staffel + '/' + releasename + '.' + staffel + 'E' + str(episodennr).zfill(2) + foldersplit[1]):
                    print('Rename folder ---> ' + releasename + '.' + staffel + 'E' + str(episodennr).zfill(2) + foldersplit[1] + ' OK')
                else:
                    print('Rename folder ---> ' + releasename + '.' + staffel + 'E' + str(episodennr).zfill(2) + foldersplit[1] + ' FAiLED')
                episodennr +=1
            print('--------')
        print('--------')
    else:
        print(" Pfad existiert nicht! " + workdir)
def CreateFolder(cf_workdir):
    if os.path.exists(cf_workdir):
        cf_staffeln = os.listdir(cf_workdir)
        cf_staffeln.sort()
        for cf_staffel in cf_staffeln:
            cf_dateien = os.listdir(cf_workdir + '/' + cf_staffel)
            cf_dateien.sort()
            for cf_datei in cf_dateien:
                cf_ordnername = re.split('.[a-z]{3}$', cf_datei)
                os.mkdir(cf_workdir + '/' + str(cf_staffel) + '/' + cf_ordnername[0])
                os.replace(cf_workdir + '/' + str(cf_staffel) + '/' + cf_datei, cf_workdir + '/' + str(cf_staffel) + '/' + cf_ordnername[0] + '/' +  cf_datei)
                if os.path.exists(cf_workdir + '/' + str(cf_staffel) + '/' + cf_ordnername[0] + '/' +    cf_datei):
                    print(' Create folder and move file --> ' + cf_ordnername[0] + '/' + cf_datei + ' OK')
                else:
                    print(' Create folder and move file --> ' + cf_ordnername[0] + '/' + cf_datei + ' FAiLED')
    print('--------')

if __name__ == '__main__':
    main()
