def main():
    ##################################################
    # Comlete your code here
    ##################################################
    pass
original_str= "Python Programming"
sub1= original_str [: -12] # extract the first substring 'Python'
sub2= (original_str.split()[1]) # extract the second substring 'Programming'
merge_str = sub2 + sub1

print (sub2)
print (sub1)
print (merge_str)
if __name__ == '__main__':
    main()
