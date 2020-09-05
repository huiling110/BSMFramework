#Ensure you source crab and setup voms certificate
#for filename in Legacy*/crab_Legacy*/; do
for filename in crab_Legacy*/; do
  echo $filename
  crab resubmit $filename
done
