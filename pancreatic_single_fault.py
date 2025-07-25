def pancreatic_single_fault (fault1, x1, x2, x3, x4, x5, x6, x7, x8):
#inputs
  P16 = 1 
  KRAS = 0
  EGF = 0 
  TGFalpha = 0
  HBEGF = 0
  NRG1 = 0
  LKB1 = 1
  PTEN = 1
  IGF = 0
  ALK = 0
  DNA_Damage = 1
  TGFbeta = 0
  
  # Drugs
  palmatine = x1
  berberine = x2
  abraxane = x3
  gemcitabine = x4
  gefitinib = x5
  dacomitinib = x6
  afatinib = x7
  #erlotinib = x8
  #olmutinib = x9
  #osimertinib = x10
  #almonertinib = x11
  #icotinib = x12
  GANT61=x8

  
  if fault1 == 1:
    EGFR = 1 
  else:
    EGFR = int (EGF or TGFalpha or HBEGF)

  if fault1 == 2:
    ERBB2 = 1 
  else:
    ERBB2 = int(EGF or TGFalpha or NRG1)
  
  if fault1 == 3:
    IGFR = 1
  else:
    IGFR = int(IGF)
  
  if fault1 == 4:
    ATM = 1
  else:
    ATM = int(not (DNA_Damage))
  
  if fault1 == 5:
    TGFBR12 = 1
  else:
    TGFBR12 = int(TGFbeta and (not berberine) and (not afatinib))
  if fault1 == 6:
    SMAD = 1
  else:
    SMAD = int (TGFBR12)  
  if fault1 == 7:
      RAS = 1
  else:
      RAS = int((KRAS and (not berberine)and (not gefitinib)) or ALK)
  if fault1 == 8:
    RAF = 1
  else:
    RAF = int(RAS and (not berberine)and (not gefitinib))
  
  if fault1 == 9:
    MEK = 1
  else:
    MEK = int(RAF and (not gefitinib))
  
  if fault1 == 10:
    JAK = 1
  else:
    JAK = int((EGFR and (not gefitinib) and (not afatinib) and (not dacomitinib)) or  (ERBB2 and (not afatinib) and (not dacomitinib)))
  if fault1 == 11:
    STAT = 1
  else:
    STAT = int(JAK and (not gemcitabine))
  
  if fault1 == 12:
    IRS = 1 
  else:
    IRS =  int(IGFR)
     
  if fault1 == 13:
    PI3K = 1
  else:
    PI3K = int((STAT and (not gefitinib)and (not palmatine) and (not dacomitinib) and (not afatinib)) or IRS or (EGFR and (not gefitinib) and (not afatinib) and (not dacomitinib)) or  (ERBB2 and (not afatinib) and (not dacomitinib)) or (RAS and (not berberine) and (not gefitinib)))
  
  if fault1 == 14:
    PIP3 = 1
  else:
    PIP3 = int((PI3K and (not berberine)and (not palmatine) and (not gefitinib) and (not dacomitinib) and (not afatinib)) or (not (PTEN or abraxane)))
  if fault1 == 15:
    PKB_AKT = 1
  else:
    PKB_AKT = int(PIP3)
  if fault1 == 16:
    AMPK = 0
  else:
    AMPK = int(LKB1)
  
  if fault1 == 17:
    RacGEF = 1
  else:
    RacGEF = int(PIP3)
  
  if fault1 == 18:   
    ERK = 1
  else:
    ERK = int(MEK and (not afatinib)and (not gefitinib) and (not dacomitinib))  
  if fault1 == 19:
    PDPK = 1 
  else:
    PDPK = int(PIP3)    

  if fault1 == 20:
    JNK = 1
  else:
    JNK = int(MEK and (not afatinib)and (not gefitinib) and (not dacomitinib))
  
  if fault1 == 21:
    RalGDS = 1
  else:
    RalGDS = int(KRAS and (not berberine)and (not gefitinib))
  
  if fault1 == 22:
    GLI1 = 1
  else:
    GLI1 = int((ERK and (not berberine)and (not gefitinib) and (not afatinib) and (not palmatine)) or SMAD)      
  
  if fault1 == 23:
    DAXX = 0
  else:
    DAXX = int (not TGFBR12)

  if fault1 == 24:
    ASK1 = 0
  else:
    ASK1 = int (DAXX)
    
  if fault1 == 25:
    RAL = 1
  else:
    RAL = int(RalGDS) 
  
  if fault1 == 26:
    MKK = 0
  else:
    MKK = int(ASK1)
  
  if fault1 == 27:
    RalBP1 = 0 
  else:
    RalBP1 = int(not(RAL))
  
  if fault1 == 28:
    PLD1 = 1 
  else:
    PLD1 = int(RAL)
  if fault1 == 29:
    P38 = 0
  else:
    P38 = int (MKK)
  if fault1 == 30:
    RAC = 1
  else:
    RAC = int((not RalBP1) or RacGEF)      
      
  if fault1 == 31:
    IKK = 1
  else:
    IKK = int(PKB_AKT and (not palmatine) and (not berberine) and (not gefitinib) and (not dacomitinib) and (not afatinib))
  if fault1 == 32:
    PA = 1
  else:
    PA = int(PLD1)

  if fault1 == 33:    
    NFKB = 1
  else:
    NFKB = int(IKK or RAC)        
  if fault1 == 34:
    TSC1by2 = 0 
  else:
    TSC1by2 = int((not(PKB_AKT and (not palmatine) and (not berberine) and (not gefitinib) and (not dacomitinib) and (not afatinib))) and (AMPK or berberine)) 
    
  if fault1 == 35:
    MDM2 = 0
  else:
    MDM2 = int(not (ATM))

  if fault1 == 36:
    P53 = 0
  else:
    P53 = int(MDM2 and P38)      

  if fault1 == 37:     
    BRCA2 = 0
  else:
    BRCA2 = int(P53 or gemcitabine )
  if fault1 == 38:     
    RHEB = 1
  else:    
    RHEB = int (not TSC1by2)
  if fault1 == 39:       
    mTOR = 1
  else:
    mTOR = int(RHEB or PA)
  if fault1 == 40:   
    RPS6KB = 1
  else:
    RPS6KB = int ((mTOR and (not berberine)) or (ERK and (not berberine)and (not gefitinib) and (not afatinib) and (not palmatine)) or PDPK)
  if fault1 == 41:   
    GSK3 = 0
  else:
    GSK3 = (not JNK)
  if fault1 == 42:   
    BAD = 0
  else:
    BAD = int ((not(PKB_AKT and (not palmatine) and (not berberine) and (not gefitinib) and (not dacomitinib) and (not afatinib))) and (not RPS6KB))
  if fault1 == 43:   
    CyclinD1 = 1 
  else:
    CyclinD1 = int(JNK or (not (GSK3 or gefitinib)) or (not(P16)) or (ERK and (not berberine)and (not gefitinib) and (not afatinib)))
  if fault1 == 44:   
    P21 = 0
  else:
    P21 = int((P53 or gemcitabine) and P16)
  if fault1 == 45:   
    CDK4by1 = 1 
  else:
    CDK4by1 = int((CyclinD1 and (not GANT61) and (not palmatine) and (not dacomitinib) and (not gefitinib)) or (not P16) or (not (P21 or abraxane))) 
  if fault1 == 46 :       
    Rb = 1 
  else:
    Rb = int(CDK4by1 and (not abraxane))
  if fault1 == 47:       
    RAD51 = 0
  else:
    RAD51 = int(BRCA2)
  if fault1 == 48:       
    P48 = 0
  else:    
    P48 = int(P53 or gemcitabine)
  if fault1 == 49:       
    BCL_XL = 1
  else:
    BCL_XL = int(((not BAD) or RPS6KB or (STAT and (not gefitinib) and (not palmatine) and (not dacomitinib) and (not afatinib))) or ((PKB_AKT and (not palmatine) and (not berberine) and (not gefitinib) and (not dacomitinib) and (not afatinib)) or (GLI1 and (not GANT61))))
     
  SRFELK1 = int((ERK and (not berberine)and (not gefitinib) and (not afatinib) and (not palmatine)) and RPS6KB)
  SP1 =  int((ERK and (not berberine)and (not gefitinib) and (not afatinib) and (not palmatine)))
  E2F = int(Rb)
  FOS_JUN = int(RPS6KB and JNK)
  BAX = int((P53 or gemcitabine) and (not (BCL_XL and (not abraxane) and (not GANT61))))
  SRFELK4 = int(JNK and RPS6KB)
  VEGF= int((STAT and (not gefitinib) and (not palmatine) and (not dacomitinib) and (not afatinib)) or (NFKB and (not berberine) and (not palmatine))) 
  DNA_Repair = int(RAD51 and P48)

  
  output1 = [SRFELK1, SP1, E2F, FOS_JUN, BAX, SRFELK4, VEGF, DNA_Repair]
  output2 = [0,0,0,0,1,0,0,1] # Ideal Output
  
  # Check the difference in outputs
  a = 0
  b = 0
  c = 0
  d = 0

  for i in range(8):
     if output1[i] == 1 and output2[i] == 1:
        a += 1
     elif output1[i] == 0 and output2[i] == 1:
        b += 1
     elif output1[i] == 1 and output2[i] == 0:
        c += 1
     elif output1[i] == 0 and output2[i] == 0:
        d += 1

  output = ((b + c) ** 2) / ((a + b + c + d) ** 2)
  return(output)
