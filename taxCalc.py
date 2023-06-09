#File to calculate the amount of taxes a user pays
def taxCalc(quartInc, quartDeduc, alternativeMinimTax, taxCredits, otherTaxes, incomeTaxWith, status):
  '''
  Explination of function inputs:
    quartInc = Quartely Income
    quartDeduc = Quarterly Deduction
    alternativeMinimTax = Alternative Minimum Tax
    taxCredits = Tax Credits
    otherTaxes = Other Taxes
    incomeTaxWIth = Withheld Income Tax
    status = filing status ('married-j', 'maried-s', 'head', or 'single')
  '''
  #Calculate Number of taxes here
  annualIncome = quartInc * 4
  deduction = 0
  line4 = 0
  line8 = 0
  line9 = 0
  line11 = 0
  line14 = 0

  totalTax = 0
  socialSecurityTax = 0
  medicareTax = 0
  incomeTax = 0
  
  
  # calculates income tax
  if annualIncome > 13850:
    deduction = quartDeduc * 4
  else:
    deduction = 13850
  line3 = annualIncome - deduction
  if line3 > 578125:
    line4 = 174238.25 + (line3 - 578125) * 0.37
  elif line3 > 231250:
    line4 = 52832 + (line3 - 231250) * 0.35
  elif line3 > 182100:
    line4 = 37104 + (line3 - 182100) * 0.32
  elif line3 > 95375:
    line4 = 16290 + (line3 - 95375) * 0.24
  elif line3 > 44725:
    line4 = 5147 + (line3 - 44725) * 0.22
  elif line3 > 11000:
    line4 = 1100 + (line3 - 1100) * 0.12
  else:
    line4 = line3 * 0.1

  line6 = alternativeMinimTax + line4
  if (line6 - taxCredits) < 0:
    line8 = 0
  else:
    line8 = line6 - taxCredits
  if line3 > 0:
    line9 = line3 * 0.9235 * 0.153
  if (line8 + line9 + otherTaxes) > 0:
    line11 = line8 + line9 + otherTaxes
  line12 = line11 * 0.9
  if (line12 - incomeTaxWith) > 0:
    line14 = line12 - incomeTaxWith
  totalTax = line14 / 4
  totalTax = round(totalTax, 2)
  totalTax = str(totalTax)
  return totalTax
  '''
  Returns the number of taxes a user pays in 4 catagories:
    Social Security
    Medicare
    Income Tax
    Total Tax
  '''