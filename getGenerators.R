getGenerators<- function(n)# funkcja przyjmuje numer grupy
{
  generators<-c()
  for (ints in seq (2,n,1))
  {
    outcomes<-c()
    for (powers in seq(1,n-1,1))
    {
      power.result<-ints^powers
      modulo.res<-power.result%%n
      if (modulo.res %in% outcomes)
      {
        break()
      }
      else
        outcomes<-c(outcomes,modulo.res)
      if(powers == n - 1)
        generators<-c(generators, ints)
        
    }
  }
  return(generators)
}
# odwrotnosc w modulko
modulko<-0
liczba <- 6
grupa <- 15
zero <- 0
while (modulko!=1)
{
  zero <- zero + liczba
  print(zero)
  modulko <- zero%%grupa
  print(modulko)
  
}
# sprawdzanie czy 2 jest generatorem w modulko

for (i in seq(1,16)){
  print(2^i)
  print("modulo:")
  print((2^i) %% 17)
}


# logarytm w modulko
modulko<-0
liczba <- 5
grupa <- 19
potega <- 0
while (modulko!=8)
{
  tmp = liczba ^ potega
  print(paste("potega 5: ",as.character(potega)))
  modulko<- tmp %% grupa
  print(modulko)
  potega <- potega + 1
}









