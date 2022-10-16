Program to work with fastq files.

The program filters the reads:
1. According to GC-content.
2. According quality.
3. According length.
Result will be saved in file.

The program consist from some functions:
- Function for calculation GC-content
- Function for calculating average quality
- Function for checking if a file exists
- 'Main' function.

The function 'main' takes the following arguments:
1. input_fastq - the path to the file that is fed to the input of the program (uncompressed fastq file).
2. output_file_prefix - prefix of the path to the file where the result will be written. 
3. gc_bounds - interval of GC-content (in percent) for filtering (default is (0, 100)).
4. length_bounds - length interval for filtering (default is (0, 2**32)).
5. quality_threshold - average read quality threshold for filtering, default is 0 (phred33 scale).
6. save_filtered - whether to save filtered reads, default is False.