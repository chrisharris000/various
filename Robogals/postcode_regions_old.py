pcode_to_rgn = {}

data = """2000 - 2019	Central & Northern Sydney
2020	Southern & South Western Sydney
2021 – 2037	Central & Northern Sydney
2038 – 2041	Western Sydney & Blue Mountains
2042 – 2044	Central & Northern Sydney
2045 – 2047	Western Sydney & Blue Mountains
2048	Central & Northern Sydney
2049	Southern & South Western Sydney
2050	Central & Northern Sydney
2052 - 2114	Central & Northern Sydney
2115 – 2118	Western Sydney & Blue Mountains
2119 – 2122	Central & Northern Sydney
2123 - 2125	Western Sydney & Blue Mountains
2126	Central & Northern Sydney
2127 – 2128	Western Sydney & Blue Mountains
2130 – 2136	Southern & South Western Sydney
2137 – 2140	Western Sydney & Blue Mountains
2141	Southern & South Western Sydney
2142	Western Sydney & Blue Mountains
2143	Southern & South Western Sydney
2144 – 2158	Western Sydney & Blue Mountains
2159	Central & Northern Sydney
2160	Western Sydney & Blue Mountains
2161 – 2166	Southern & South Western Sydney
2167 – 2179	Southern & South Western Sydney
2190 – 2203	Southern & South Western Sydney
2204	Central & Northern Sydney
2205 – 2234	Southern & South Western Sydney
2250 - 2311	Hunter & Central Coast
2312	North Coast & Mid North Coast
2313 - 2339	Hunter & Central Coast
2340 - 2385	New England
2386 - 2387	Western NSW
2388 - 2411	New England
2415 - 2425	Hunter & Central Coast
2426 - 2427	North Coast & Mid North Coast
2428 - 2456	North Coast & Mid North Coast
2460 - 2490	North Coast & Mid North Coast
2500 - 2551	Illawarra & South East NSW
2555 – 2560	Southern & South Western Sydney
2563 – 2574	Southern & South Western Sydney
2575 – 2584	Illawarra & South East NSW
2585 – 2594	Riverina
2600 – 2633	Illawarra & South East NSW
2640 – 2663	Riverina
2665 - 2669	Riverina
2671 - 2672	Western NSW
2675	Riverina
2678	Riverina
2680 – 2717	Riverina
2720	Riverina
2721	Western NSW
2722 - 2739	Riverina
2745 - 2751	Western Sydney & Blue Mountains
2752	Southern & South Western Sydney
2753 – 2786	Western Sydney & Blue Mountains
2787 - 2800	Western NSW
2803	Riverina
2804 - 2806	Western NSW
2807	Riverina
2808 - 2880	Western NSW
2898 - 2899	North Coast & Mid North Coast
2900 – 2914	Illawarra & South East NSW"""

for line in data.split("\n"):
    postcode_range, region = line.split("\t")

    if len(postcode_range) == 4:
        pcode_to_rgn[int(postcode_range)] = region

    else:
        start_val, end_val = postcode_range[:4], postcode_range[-4:]
        for postcode in range(int(start_val), int(end_val) + 1):
            pcode_to_rgn[postcode] = region

def postcode_to_region(postcode):
    return pcode_to_rgn[postcode]