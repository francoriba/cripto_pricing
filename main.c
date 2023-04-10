#include "cdecl.h"

int PRE_CDECL asm_main( void ) POST_CDECL; 
double PRE_CDECL convert_to( double, double) POST_CDECL; 

int data_interface(double btc_usd, double eth_usd, double ltc_usd, double rate_ars, double rate_eur){
    double btc_ars, btc_eur, eth_ars, eth_eur, ltc_ars, ltc_eur; 

    //bitcoin convertions
    btc_ars = convert_to(btc_usd, rate_ars);
    btc_eur = convert_to(btc_usd, rate_eur);

    //ethereum convertions
    eth_ars = convert_to(eth_usd, rate_ars);
    eth_eur = convert_to(eth_usd, rate_eur);

    //litecoin convertions
    ltc_ars = convert_to(ltc_usd, rate_ars);
    ltc_eur = convert_to(ltc_usd, rate_eur);
    
    return btc_ars ;}
