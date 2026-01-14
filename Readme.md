
# HIT137 – Software Now  

## **Charles Darwin University**

This repository contains the complete solutions and collaboration evidence for **Assignment 2** of *HIT137 – Software Now*.

**Teacher:** Abdallah Al Tawara

---

## Team Members

- **Saimon Dahal** (S399238)  
- **Lamim Hasan** (S397782)  
- **Mir Saifur Rahman** (S398452)  
- **Omar Faruk** (S394752)

---

## Team Members Contributions

### Saimon Dahal (S399238)
- Built the encryption module for Question 1.  
- Tested the decryption logic and identified a character-collision bug in the encryption process.  
- Ran boundary and negative tests across all three questions.  
- Found a logical bug in Question 3 where edges were divided into 3 segments instead of 4.  
- Helped write and clean up the project documentation.

### Mir Saifur Rahman (S398452)
- Wrote the initial decryption module for Question 1.  
- Implemented the verification logic for Question 1.  
- Reviewed the encryption portion and tested edge cases.  
- Helped update documentation for final submission.

### Lamim Hasan (S397782)
- Reviewed all programs for errors and logical issues.  
- Completed the full solution for Question 3.  
- Helped resolve the character-collision bug in Question 1.  
- Improved overall code quality and flow.

### Omar Faruk (S394752)
- Built all data handling for Question 2 (file merging and reshaping temperature values).  
- Grouped months into Australian seasons.  
- Calculated seasonal averages and identified the most variable stations.  
- Tested edge cases and saved results in the required output files.

---

## Question 1

### `encrypted_text.txt`
```text
Ptq xbuow nyvdu rve vbywz vcqy atq xmgf pvs nquqmat atq ztmpf duxxvdz. Ptq pvs, zamyaxqp ryvy tuz wqmoqrbx mraqyuvvu umw, xbuowxf yuzqz mup otmzqz mraqy atq yuzotuqcvbz rve. 

<<<Ptyvbst cunymua yqmpvdz mup wmza nbgguus nqqtucqz atqf ymoq, puzabynuus m rxvow vr xbmuxz atma zomaaqy uuav atq oyuzw mbabyu zwf.>>> Ptq rve, xbuaq wxqmzqp duat tuz oxqcqy wymuw, pmztqz uuav tuz ovgf bupqysyvbup pqu dtuxq atq pvs, uvd qetmbzaqp ryvy atq gqmxvbz wbyzbua, yqabyuz av tuz rmcvyuaq zwva bupqy atq dtuzwqyuus nymuotqz av yqzbyq tuz xbuqa zxbynqy.
````

### `decrypted_text.txt`

```text
The quick brown fox jumps over the lazy dog beneath the shady willows. The dog, startled from his peaceful afternoon nap, quickly rises and chases after the mischievous fox. 

<<<Through vibrant meadows and past buzzing beehives they race, disturbing a flock of quails that scatter into the crisp autumn sky.>>> The fox, quite pleased with his clever prank, dashes into his cozy underground den while the dog, now exhausted from the zealous pursuit, returns to his favorite spot under the whispering branches to resume his quiet slumber.
```

---

## Question 2

### `average_temp.txt`

```text
Summer: 32.1°C
Autumn: 27.3°C
Winter: 21.1°C
Spring: 27.4°C
```

### `largest_temp_range_station.txt`

```text
BOURKE-AIRPORT-AWS: Range 24.4°C (Max: 43.0°C, Min: 18.5°C)
```

### `temperature_stability_stations.txt`

```text
Most stable: DARWIN-AIRPORT: StdDev 1.2°C
Most variable: WAGGA-WAGGA-AMO: StdDev 6.9°C
```

---

## Question 3
![Question 3 Output](https://github.com/saimon-dahal/HIT137-assessment2-sydn17/blob/1a0b590536de832029d0ce8a3581f59bd6574dc4/question3_solution.png)

