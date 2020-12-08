# Overview

## Introduction

This project consists of two parts: 

1. A mathematical exploration of the history and math behind the Hamming Code (7, 4).
2. A program that simulates the process of encoding, correcting, and decoding as described by the Hamming Code.

To understand what the Hamming Code is, skip to the background section first to get an understanding of how the process is meant to work. Then, you can run the sample program to see it in action! 

## Setup



## Encoding

The sender.py file is responsible for encoding a given bit string.


## Correction + Decoding

The receiver.py file is responsible for encoding a given bit string.

# Background

## Introduction

Error correction and detecting codes are an ever-increasingly important concept that is still being used in modern day computer science and telecommunication. The transmission of data across unreliable communications channels, also known as "Noisy" channels, often leads to small sections of data being mutated. There are a large number of applications of error checking, ranging from products used by millions of consumers, to cutting edge technology used in military settings. Voyagers 1 and 2 employed a variety of different code correction schemes, most notably the Reed-Solomon and Reed-Muller codes, to deliver detailed images and information from the probes back to Earth. That is, the codes were responsible for correcting information sent from Saturn and Jupiter, which often times became diluted due to long distances and signal conservation used in the probes, back to Earth. Hard disks on computers and other devices use error correcting codes to fix corrupted data. Wireless LAN and Ethernet use a variety of different schemes to correct important header information and minimize mistakes in transmitted information. The importance of error correction codes cannot be understated; without it, the cost of transmitting erroneous information would be astronomical. More importantly, many of the comforts of daily life, namely WIFI, as well as the latest technological advancements would be unattainable.

So, who should we thank for creating the field of code correction? There were a number of different pioneers, but among those individuals is one whose name is so ingrained in the study of code correction that there have been a number of rudimentary error-code correction schemes named after him: Richard Hamming.

## Richard Hamming

Born in 1915 in Chicago, Richard Hamming was an able mathematician, but wanted to study engineering in college. Unfortunately (or maybe fortunately), he was never offered a scholarship to a school that had an engineering department during a time when money was hard to come by (Great Depression), and had to settle for a degree in Mathematics at the University of Chicago. Later in life he would reflect how this turn of events was actually for the better, as he believed that the engineers were the ones doing the dirty work, while the mathematicians were engrossed in interesting research at the boundaries of what was known. He continued his mathematical studies, and received a PhD in the field at the University of Illinois.

Post-graduation, he worked as an assistant professor at the University of Louisville. He would later join the Manhattan Project at the eve of World War II, and was responsible for programming IBM machines that developed the equations for the physicians. He considered himself a "Computer Janitor", as his only responsibility was to maintain the computers, and perform the computations formulated by the physicians. He was even interrogated by the FBI for buying the vehicle of a German spy who worked at the laboratory, although he was unaware that the individual was a spy.

After his tenure at Los Alamos, he joined the Bell Laboratories in 1947. His work at Bell Labs is what he is mainly known for, as it was here that he led research on error detecting and error correcting codes. However, this was not his initial area of study. As a matter of fact, it was only the error prone calculations that were conducted on the machines used in the Lab that led him to develop the different error correcting schemes. By 1950, he would write a foundational paper that marked the emergence of a field in error correction, one that would later result in the Turing award, the most prestigious award in computer science, to be given to Hamming for the search he had done in error correction. But Hamming's research went beyond error correction, as there were a number of different areas that Hamming explored, including regular numbers, early age computing, and programming languages.

When his time at Bell Laboratories came to an end, so did his career in research, as he recalled while teaching at the Naval School, "When I left BTL, I knew that that was the end of my scientific career. When I retire from here, in another sense, it's really the end." His philosophy when it came to education is quite profound, as he believed that education should be centered around learning how to learn rather than centering the education on the content itself (something I do agree with). He found the way university education to be very boring, and comprised of reading dull textbooks and a lack of applications to truly appreciate the importance of mathematics.

His retirement from teaching in 1997 marked the end of his career in teaching, as well as the end of his life as he perished soon after his last lecture. However, as mentioned before, his contributions to society and mathematics will forever be remembered, not simply by the traces of his name left behind in well-unknown principles and algorithms, but also the impact of his ideas on modern day discoveries in a litany of different fields.

# Hamming Code (7,4)

## Top-Level Description

Among the most foundational, and simplest code correcting schemes that Richard Hamming uncovered in his paper in 1950 was the Hamming(7,4) code.

The Hamming(7,4) code is an error correcting code for binary strings, that is, a number comprised of digits that are either 0 or 1. Given a binary string, for every four bits of data, the Hamming(7,4) code would perform an encoding by attaching 3 additional bits, known as parity bits, and attaches these 3 bits to the original 4 bit string subsequence to create a 7 bit subsequence. How these 3 parity bits are created is dependent on the original 4 bit string subsequence, and will be discussed in the next section. After the string of 7 bit subsequences is sent across a communication channel to the receiver, the receiver would then check if the bit string is erroneous using an algorithm that takes advantage of the 3 added parity bits, and fixes all the bits that need to be changed, and strips each subsequence of the 3 added bits to obtain the original bit string.

Thus, the Hamming Code is divided into two parts. One part is the process for the sender, who first encodes their 4-bit string to a 7-bit string. Once the 7-bit string is received by the receiver across a noisy channel, it is first corrected of any possible mutations, and then decoded back to its 4-bit string format.

You might be wondering, why do we need to add so many additional bits on top of the original bit string? Well, sending just the original bit string across a communication channel often times results in bit mutations, where bits are flipped. There would be no way of telling which bit is accurate if we sent the original bit string alone. As a matter of fact, the Hamming(7,4) code is fairly efficient when it comes to implementation. The most trivial code-correcting scheme would send multiple copies of the same bit string. For instance, there could be a code-correcting scheme could send three copies of the same bit string instead of just one. If there is a certain bit that not all three copies agree on after being sent across the channel, whichever bit, 0 or 1, appears twice across the three copies would be the chosen as the correct bit (majority rules). This scheme may be accurate for some cases, but is highly inefficient in that for every bit in the original bit string, an additional 2 new bits would need to be added. The Hamming(7,4) code is far more efficient, as only  $\frac{3}{4}$ bits would be added for each bit in the original bit string. As you can probably tell, code correction seems like a rather simple subject when in fact it is a rather complex subject when you take into account the efficiency and effectiveness of the different code-correcting algorithms.

There are limitations to the Hamming(7,4) code, and by no means is this code the best code-correcting algorithm. First, for each generated 7-bit subsequence, the algorithm can only correct a single-bit error, and can only detect two-bit errors. Hence, the Hamming(7,4) is not effective for channels that are prone to burst errors, which are errors that occur on contiguous bits. Secondly, there are error-correcting codes that are more efficient and require fewer additional bits to be sent on top of the original bit string. However, most of the times there is a tradeoff between accuracy, and space conservation, so the choice of error-correcting codes depends heavily on most common errors, as well as the frequency of those errors for a given noisy channel.

The code led to the advancement of other code-correction schemes, and many of its central ideas, like the introduction of parity bits. The Hamming(7, 4) is still being used as the base for the Steane code, which is used in quantum error correction.

## Math

Let's assume that we have already divided up our bit string into four bit sequences. Now, we will call these bits $b_1, b_2, b_3, b_4$ respectively.

As mentioned previously, the three parity bits are dependent on the values of the original bits. Let's call the 3 parity bits $p_1, p_2, p_3$. $p_1$ is dependent on $b_1, b_2, b_4$, $p_2$ is dependent on $b_1, b_3, b_4$, and $p_3$ is dependent on $b_2, b_3, b_4$. For each parity bit, its value is determined on how many of the bits that it is dependent on are 1s. If the number of bits that it is dependent on is odd, then the parity bit would be 1. If the number of bits it is dependent on is even, then the parity bit is even.

It can be seen easily that the number of bits that are equal to 1 for a given number of bits is simply the the sum of those bits, as if a bit isn't equal to 1 it is equal to 0. Next, for any given even integer, we know that it can be represented as $2n$, where $n$ is also an integer. We also know that for any given odd integer can be represented as $2n + 1$, where n is an integer. Finally, we know that an odd number modulo 2 is equal to 1, as $(2n + 1) \mod 2 = (2n) \mod 2 + (1) \mod 2  = (1) \mod 2$. For an even number modulo 2 is equal to 0, as $2 \mod 2 = 0 \mod 2$. Lastly, because of all these properties, as well as our definition of the parity bits described above, we can determine the following parity bits like so: $p_1 = (b_1 + b_2 + b_4) \mod 2, p_2 = (b_1 + b_3 + b_4) \mod 2, p_3 = (b_2 + b_3 + b_4) \mod 2$.

Another notable observation is that the parity of the parity bit, along with the three bits it is dependent on, that is the number of ones in the sequence of bits consisting of the parity bit and the three bits, will always be even in the case where there is no error. For instance, let's call a parity bit $a$, and let it be dependent on $b, c, d$. We know that $a = (b, c, d) \mod 2$. We can calculate the parity of $a, b, c, d$ easily and in the same way we calculated the parity of $b, c, d$. That is, $(a + b + c + d) \mod 2 = (((b + c + d) \mod 2) + b + c + d) \mod 2 = ((b + c + d) + b + c + d) \mod 2 = (2b + 2c + 2d) \mod 2 = 2(b + c + d) \mod 2 = 0$. Hence, the parity of the four bits will always be 0 (in other words, the sum of the bits is even, and the number of bits that are 1 is even). 

Because of this observation, we can tell if an error has occurred, simply by looking at the three parities that represent the parities of each 4 bit grouping (1 parity bit + 3 normal bits). In the diagram below, the green circle represents one grouping, which contains the bits $p_1, b_1, b_2, b_4$. The red and blue circle contains a different set of bits, which can be easily seen. As we have already proved above, the parity of the bits in each circle must be even if no error has occurred. If there is an error (that is, a single bit error), the parity of one or more of the set of bits represented by the circles will be 1, as the number of bits that are 1 would be odd.

First, let's make an assumption that the error at hand is a 1 bit error, where a single bit in our bit string of length 7 is erroneous. Then given the parities of the three groupings of bits, we would know which bit out of the 7 bits is flipped.

![Venn Diagram](/images/venn.png)

Diagram 1: Venn diagram showing relationship of parities of the 3 parity bit sets.

The Venn Diagram shown in Diagram 1 is instrumental for our understanding of how to identify where the bit error's location is. Each of the circles represents the collection of bits that are grouped together, which was discussed above. If there is no bit error, each of the circles would have a parity of 0, which was also proved above. If there is a single bit error, the parities of one or more of these circles would not be 0.

Let $c_1$ be the parity of the green circle (circle on the left), $c_2$ be the parity of the red circle (circle on the right), and let $c_3$ be the parity of the blue circle (bottom circle). By definition of parity, $c_1 = (p_1 + b_1 + b_2 + b_4) \mod 2, c_2 = (p_2 + b_1 + b_3 + b_4) \mod 2, c_3 = (p_2 + b_2 + b_3 + b_4) \mod 2$. Because there are 7 different bits, there are a total of 7 different errors. Hence, we can see which of the three parities, $c_1, c_2, c_3$ change for each different error. It turns out, an error on all 7 bits have a different combination of parities for $c_1, c_2, c_3$. We can see this quite easily, as if there is a one bit error, we can locate the error by the following reasoning: if $c_i$ has odd parity, that means that the error is one of the four parity bits, and if $c_i$ has even parity, we know that none of its bits are erroneous. The reasoning for the second part is rather simple, as a single bit error would flip at most one of the four bits per group of bits, which means that the resulting parity would be odd.

### Encoding

Given a bit string of length 4, we first want to encode this bit string to a length of 7 by appending the 3 parity bits to this bit string. In essence, if we divide the bit string into its 4 bits, $b_1, b_2, b_3, b_4$, we can construct a vector in $R^4$, and we want to map this vector to a vector in $R^7$. Hence, we know that there is a linear map $T: R^4 \rightarrow R^7$, and its corresponding matrix would be from $7 \times 4$.

For a given vector in $R^4$, we want to map it a vector in $R^7$ such that the first four elements in that vector are the same. The following three elements in the vector will correspond to the three parity bits, $p_1, p_2, p_3$, will be found based off of the bits that they are dependent upon.

What should the transformation $T$ be then? $T(b_1, b_2, b_3, b_4) = (b_1, b_2, b_3, b_4, b_1 + b_2 + b_4, b_1 + b_3 + b_4, b_2 + b_3 + b_4)$. The first four elements in the range are obtained easily, as they are simply the bits. The latter three elements represent the parities (without modular division), as $p_1 = b_1 + b_2 + b_4, p_2 = b_1 + b_3 + b_4, p_3 = b_2 + b_3 + b_4$.

That leads us with a matrix $A$ which is the matrix of $T$ with respect to the standard basis that is equal to $A = \begin{bmatrix} 
1 & 0 & 0 & 0 \\ 
0 & 1 & 0 & 0 \\ 
0 & 0 & 1 & 0 \\ 
0 & 0 & 0 & 1 \\
1 & 1 & 0 & 1 \\ 
1 & 0 & 1 & 1 \\
0 & 1 & 1 & 1 
\end{bmatrix}$

However, we are not complete. Because $p_1, p_2, p_3$ are parity bits, we haven't done our modular division yet. Hence, the matrix/column vector we want to send is actually $Ax \mod 2$, which will give us the accurate bit representation of the 7 bit vector.

### Checking for Correctness

The constructed matrix for decoding that corresponds with $A$ is:

$B = \begin{bmatrix}
1 & 1 & 0 & 1 & 1 & 0 & 0 \\
1 & 0 & 1 & 1 & 0 & 1 & 0 \\
0 & 1 & 1 & 1 & 0 & 0 & 1
\end{bmatrix}$

$B$ is the transformation that will take our 7-bit vector and turn it into the 3-bit vector with elements corresponding to $c_1, c_2, c_3$ as described in a previous section. Given the values of $c_1, c_2, c_3$, we will be able to determine whether or not an erroneous solution is present. $B(b_1, b_2, b_3, b_4, p_1, p_2, p_3) = (b_1 + b_2 + b_4 + p_1, b_1 + b_3 + b_4 + p_2, b_2 + b_3 + b_4 + p_3)$. The matrix corresponding to this transformation is simply the one shown above. Lastly, because we want the resulting matrix to be in bit notation, we would simply mod the resulting vector similar to the process we did for constructing our 7-bit vector.

### Correction

The interesting thing is that when applied to linear algebra, a non-erroneous resulting bit vector can be seen as mapping into the null space. This is because the parity of $c_1, c_2, c_3$ would all be even (and hence equal to 0). By this logic, it can be seen that if $Bu = v$ where $v$ is the correct solution, then $v$ would be the 0 vector. Hence, any $u$ in this case would be a vector in the null space. However, because of the modular division we have to do after the matrix multiplication, this is not entirely the same thing as a mapping into the null space.

Given a vector $v$ that is in $R^7$ that we want to check for correctness, we know that $Bv = w$ will give us a vector $w \in R^3$ that will have 3 elements that represent $c_1, c_2, c_3$. As described in a previous section, whichever one of these bits has odd parity, that bit contains an erroneous dependent bit, and whichever bits have even parity, that bit doesn't contain an erroneous dependent bit. Hence, given this information, we can identify which one of the 7 bits are erroneous.

For simplicity purposes, here are the mappings to identify the incorrect bit: $(1, 0, 0) \rightarrow p_1, (0, 1, 0) \rightarrow p_2, (0, 0, 1) \rightarrow p_3, (1, 1, 0) \rightarrow b_1, (1, 0, 1) \rightarrow b_2, (0, 1, 1) \rightarrow b_3, (1, 1, 1) \rightarrow b_4$.

Once the mutated bit is identified, we can easily correct for the mutation by flipping the bit at that location. We do this by adding the unit vector corresponding to the bit that we want to flip. For instance, the unit vectors where the 1s are one of the first four elements would flip $b_1, b_2, b_3,$ or $b_4$. The latter three would flip $p_1, ..., p_3$.

Let's say $v$ is our vector in $R^7$, and $e$ is the unit vector to correct our error. Then $B(v + e)$ would map to the null space, as that would indicate that there are no more bit mistakes.

### Decoding

Once the vector has been corrected, we can decode the 7-bit vector back to its 4-bit vector form. Let's call $v$ the 7-bit vector (it is in $R^7$), and we want to find a transformation $C$ that will take it back to its original $R^4$ vector. we know that the first four elements in $v$ correspond to the bits $b_1, ..., b_4$, and the other three are the parity bits. Since we already did correction, the parity bits are no longer of use. Hence, the transformation $C$ will be the following: $C(b_1, b_2, b_3, b_4, p_1, p_2, p_3) = (b_1, b_2, b_3, b_4)$. The matrix of this transformation with respect to the standard basis would be the following:

$C = \begin{bmatrix} 
1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 0
\end{bmatrix}$

Given $Cv = w$, the vector $w$, which is in $R^4$ would be the decoded bit string that is sent over.

## Summary

Because the process of encoding, decoding, and correcting is entangled with a mathematic explanation, the process might be somewhat unclear. Here is a more concise summary of the process:

The sender has a 4-bit string that it wants to send to a receiver. The sender will encode that 4-bit string into a 7-bit string (using matrix/transformation A). This 7-bit string contains the original 4-bits, as well as 3 additional parity bits.

This bit-string is then sent through a communication channel to the receiver.

The receiver then checks if this 7-bit string is valid by using the matrix/transformation B. If it is incorrect, the receiver will correct the erroneous bit (it is assumed that there is only a 1-bit error).

Given a corrected bit string, the receiver will then decode this correct bit string using matrix/transformation C. This will turn the 7-bit string back into a 4-bit string. The resulting 4-bit string is the original string.

# References

https://en.wikipedia.org/wiki/Hamming(7,4)

https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.15.2088&rep=rep1&type=pdf

https://en.wikipedia.org/wiki/Error_detection_and_correction

https://homes.cs.washington.edu/~jrl/teaching/cseP531sp16/presentations/pres3.pdf