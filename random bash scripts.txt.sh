for p in cats river sun; do
	
	#create a gallery
	mkdir ./${p}-gallery;
	for n in $(seq 3); do
		curl http://loremflickr.com/600/400/${p}?random > ./${p}-gallery/${p}-${n}.jpg; 
	done;

	# create post .md file
	touch ./${p}-info.md;
	echo $"Title: Proyecto Identidad de "${p}"" >> "./${p}-info.md"; 
	echo $"coverimg: "./${p}-gallery/${p}-1.jpg"" >> "./${p}-info.md";
	echo $"covertext:  " >> "./${p}-info.md";
	echo >> "./${p}-info.md";   # 2 blank lines
	echo >> "./${p}-info.md";	
	echo $"Some text about the project" >> "./${p}-info.md";

done

# #pause
# read -p "Press [Enter] key to erase everything..."

# # erase
# for p in cats river sun; do
# 	rm ./${p}-info.md;
# 	rm -r ./${p}-gallery;
# done
