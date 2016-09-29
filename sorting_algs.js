// basic sorting algorithms and other stuff in javascript! 

// bubble sort
// insertion sort
// selectionSort
// merge
// merge sort


// counting sort
// radix sort
// brute force string matching
// binary search
// heapsort
// quicksort



function bubbleSort(myList){
 	//looks at each adj pair of elements and swaps if not in right order
 	// sorts an array of integers in increasing order
	var listLen = myList.length;
	for (var j = 0; j <listLen; j++){
		for (var i = 0; i < listLen; i++){

			if (myList[i] > myList[i+1]){
				var tmp = myList[i];
				myList[i] = myList[i+1];
				myList[i+1] = tmp;
			}
			
		}
	}
	console.log(myList);
}

// bubbleSort([1,0,2,5,4,3,7,6,13])


function insertionSort(myList){
 	//for each element A[i] if A[i] > A[i+1], swap until A[i] =< A[i+1]
 	// sorts an array of integers in increasing order
 	var listLen = myList.length;
 	for(var j = 0; j <listLen; j++){
 		for(var i = j; i >= 0; i--){
 			if (myList[i] > myList[i+1]){
				var tmp = myList[i];
				myList[i] = myList[i+1];
				myList[i+1] = tmp;
			} 
			//everything to the left of current index is in rel order
			// so if the "if" condition isn't true we can move on to the next index
			else {
				break;
			}
 		}
 	}
 	console.log(myList);
}


//insertionSort([1,0,2,5,4,3,7,6,13])


function selectionSort(myList){
	// sorts an array of integers in increasing order
	for (var listLen = myList.length-1; listLen >=0; listLen--){
		var largest = 0;
		var large_index = 0;
		for(var i = 0; i <= listLen; i++){
			if (myList[i] > largest){
				largest = myList[i];
				large_index = i;
			}
		}
		var tmp = myList[listLen];
		myList[listLen] = largest;
		myList[large_index] = tmp;
		
	}
	console.log(myList);
	
}


//selectionSort([1,0,2,5,4,3,7,6,13])

function merge(left,right){

	var results = [];
	var left_index = 0;
	var right_index = 0;
	var len_r = right.length;
	var len_l = left.length;
	while(left_index < left.length && right_index < right.length){
		if (left[left_index] <= right[right_index]){
			results.push(left[left_index]);
			left_index ++;
		}
		else{
			results.push(right[right_index]);
			right_index ++;
		}
	}
	if (left_index < left.length){
		results = results.concat(left.slice(left_index, len_l));
	}
	if (right_index < right.length){
		results = results.concat(right.slice(right_index,len_r));
	}

	return results;
}

// var a = [4,5,6];
// var b = [1,2,3];
// console.log(merge(a,b));


function mergeSort(myList){
	len = myList.length;
	if (myList.length == 0){
		return myList;
	}
	if (myList.length == 1){
		return myList;
	}
	var middle = myList.length/2;
	var left = mergeSort(myList.slice(0,middle));
	var right = mergeSort(myList.slice(middle,myList.length));
	
	return merge(left,right); 

}

//var myList = [1,0,3];
//console.log(mergeSort(myList));




 

