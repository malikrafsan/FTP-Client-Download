
import ftplib
import config
from timeit import default_timer as timer

def get_file(ftp_server: ftplib.FTP, file_server, file_client):
  print("<><><><><><><><><><><><><><><><><><><><><><>")
  print("Downloading file: " + file_server)
  start = timer()
  
  with open(file_client, "wb") as file:
    ftp_server.retrbinary(f"RETR {file_server}", file.write)
  
  end = timer()
  print(f"Downloaded in {end - start} seconds")
  print("<><><><><><><><><><><><><><><><><><><><><><>\n")

def main():
  ftp_server = ftplib.FTP(config.HOSTNAME, config.USERNAME, config.PASSWORD)
  ftp_server.encoding = "utf-8"

  files = config.FILES
  for file in config.FILES:
    get_file(ftp_server, file, files[file])

  ftp_server.quit()

if __name__ == '__main__':
  main()
