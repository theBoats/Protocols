# Pool-seq

## Before you begin
It is critical to assign your samples to pools to minimise batch effect. Critically any treatments should be split evenly across pools and if possible replicates as well. See examples from Jess or Graham.

### Reverse Transcription, Pooling and Exonuclease Treatment

Reagents Needed

1. 50ng RNA per sample
	|Pool seq box|
2. 10uM aliquots of each Indexed RT primer that will be used
3. 10uM aliquot of Template Switching Oligo (TSO) 
4. 10mM dNTPs 
5. Exonuclease 1
	|Smart-seq box|
6. RT: Clontech SMARTscribe 
7. 5X FS buffer
8. 100mM MgCl2
	|Protein box|
9. 100mM DTT
	|Perkins lab fridge in rack|
10. 5M betaine
	|Perkins lab fridge or RT on Graham's bench
11. SPRI Select or XP beads

> Try quantifying input RNA with Qubit assay


### RT Program for Thermocycler
42 degrees for 90 min

Ten Cycles:
50 degrees 2 min
42 degrees 2 min
70 degrees 15 min

4 degree hold

### Annealing
1. Add 50ng of RNA to a PCR tube and make up to 5uL with water
2. Add 1uL of indexed RT primer and 1uL 10mM dNTPs (Can add in ERCC here)
3. Put in thermocycler at 72 degrees for 3 min and then immediately place on ice

### RT Reaction

Make up a master mix (10uL total per sample)

1. 3.6uL SS 5X buffer
2. 0.25uL water
3. 0.25uL DTT 100mM
4. 2uL betaine 5M
5. 0.9uL MgCl2 100mM
6. 2.5uL TSO 10uM
7. 0.5uL SuperScript II RT

Add 10uL of master mix to each tube

Run RT program on thermocycler

### Pooling and Exonuclease Treatment

Pool samples by adding an equal volume of the RT reactions to a new well with a final volume of 20uL

Add 1uL of Exonuclease 1 to each pool

Place on thermocycler

37 degrees 45 min;

92 degrees 15 min;

Sub-pools were then cleaned using SPRI Select beads



Add 12uL beads to each sub pool and then follow manufacturer's instructions

Elute in 10uL water into new tubes



### cDNA Amplification

Reagents Needed

1. 20uM Enrichment Primer A
2. 20uM Enrichment Primer B
3. Kapa HiFi HotStart Ready Mix
4. SPRI or XP beads
5. QUBIT (kit and instrument)

cDNA Amplification Program (Touch-up PCR)

95 degrees 3min

Four Cycles
98 degrees 20s;
65 degrees 45s;
72 degrees 3min

Nine Cycles
98 degrees 20s;
67 degrees 20s;
72 degrees 3min;

72 degrees 5 min;
4 degree hold

Protocol

Add 1.25uL of Enrichment Primers A and B to each sub-pool

Add 12.5uL Kapa to each sub-pool

Run cDNA Amplification Program

Clean sub-pools by adding 15uL of SPRI beads and elute in 10uL water

Quantify cDNA with QUBIT (e.g. Yielded 6 ng/uL from a sub-pool of 4 RNA samples)

Dilute cDNA sub-pools to 0.2 ng/uL

> Store diluted cDNA in fridge in case some of the downstream steps don't work


### Tagment, PCR and Final Pooling



Reagents Needed

1. 0.2 ng/uL cDNA sub-pools
	|Pool-seq box|
2. 2uM Indexed Nextera i5 primers
3. 2uM Enrichment Primer A
	|Perkins -30oC freezer and glass door fridge|
4. Nextera XT Kit

*Followed the Nextera XT protocol with diluted RNA and reduced kit volumes (five-fold)*

https://emea.support.illumina.com/content/dam/illumina-support/documents/documentation/chemistry_documentation/samplepreps_nextera/nextera-xt/nextera-xt-library-prep-reference-guide-15031942-05.pdf



Tagment Program (Set lid temperature to 100 degrees)

55 degrees 3 min
10 degree hold


Tagment Protocol

Add the following volumes in the order listed to a tube for each cDNA sub-pool

1. TD (2 µl)
2. DNA (1 uL)

Pipette to mix.

3. Add 1 µl ATM to each well

Pipette 10 times to mix

> With small volumes and viscous solutions it is critical to mix the reaction thoroughly to produce consistent tagmentation

Spin down tubes

> Run thermocycler and proceed immediately to step 7 once it reaches 10 degrees because the transposome is still active

4. Add 1 µl NT to each tube

Pipette 10 times to mix

Spin down tubes

Incubate at room temperature for 5 minutes


PCR Program (Set lid temperature to 100 degrees) 

72 degrees 3 min
95 degrees 30 s

Twelve Cycles
95 degrees 10 s
55 degrees 30 s
72 degrees 30 s
72 degrees 5 min

10 degree hold

PCR Protocol

1. Add 1 uL of indexed i5 primer and 1 uL Enrichment Primer A to each tagment reaction
2. Add 3 uL NPM to each tube

Pipette 10 times to mix

Spin down tubes

Run PCR program

(Can store PCR'd tagments up to 2 days in the fridge before cleaning)



### Clean up Libraries

Prepare fresh 80% ethanol

Add 6 uL SPRI beads to each PCR tube

Shake for 2 min on Tapestation shaker

Incubate at room temperature for 5 min

Place on magnet

Discard supernatant and add 200 uL 80% ethanol

Incubate for 30 s then repeat steps 6 and 7

Use a 20 uL pipette to remove any residual ethanol and leave to dry for ~3 min (tube lids open)

Remove tubes from magnet and add 10 uL water

Shake for 2 min on Tapestation shaker

Incubate at room temperature for 5 min

Place on magnet and pipette clean PCR into a fresh tube

Run each sample on the Tapestation and pool equimolarly to the desired final concentration
