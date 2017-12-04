setwd('/Users/Rushi/Documents/Masters/ML/Project2/Project2')
gwtgwtlibrary(qdap)

Clean_String <- function(string){
  # Lowercase
  temp <- tolower(string)
  #' Remove everything that is not a number or letter (may want to keep more 
  #' stuff in your actual analyses). 
  temp <- stringr::str_replace_all(temp,"[^a-zA-Z\\s]", " ")
  # Shrink down to just one white space
  temp <- stringr::str_replace_all(temp,"[\\s]+", " ")
  # Split it
  temp <- stringr::str_split(temp, " ")[[1]]
  # Get rid of trailing "" if necessary
  indexes <- which(temp == "")
  if(length(indexes) > 0){
    temp <- temp[-indexes]
  } 
  return(unique(temp))
}

mypath = "/Users/Rushi/Documents/Masters/ML/Project2/Project2/newsgroups"
file_list <- list.files(mypath, full.names=TRUE, recursive=TRUE)
for(file in file_list){
  #splitted_data<-strsplit(file, "\\/")
  #name<-sapply(splitted_data, function(x) x[2])
  read<-readLines(file)
  read
  read<- iconv(enc2utf8(read),sub="byte")
  read
  #reading<-Clean_String(read)
  frequent_terms <- list.extend(file,freq_terms(read))
}

