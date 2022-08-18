p_schools_raw = """Penrith Public School
Penrith South Public School
Penshurst Public School
Penshurst West Public School
Petersham Public School
Picnic Point High School
Picnic Point Public School
Picton High School
Picton Public School
Pittwater High School
Plumpton High School
Plumpton Public School
Plunkett Street Public School
Port Hacking High School
Prairievale Public School
Prairiewood High School
Prestons Public School
Punchbowl Boys High School
Punchbowl Public School
Putney Public School
Pymble Public School"""

q_schools_raw = """Quakers Hill East Public School
Quakers Hill High School
Quakers Hill Public School"""

r_schools_raw = """Rainbow Street
Ramsgate Public School
Randwick Boys High School
Randwick Girls' High School
Randwick Public School
Redbank School
Regents Park Public School
Regentville Public School
Revesby Public School
Revesby South Public School
Richmond High School
Richmond Public School
Ringrose Public School
Rivendell School
Riverbank Public School
Riverside Girls High School
Riverstone High School
Riverstone Public School
Riverwood Public School
Robert Townson High School
Robert Townson Public School
Rockdale Public School
Rooty Hill High School
Rooty Hill Public School
Rose Bay Public School
Rose Bay Secondary College
Rosebank Public School
Rosehill Public School
Roselea Public School
Rosemeadow Public School
Roseville Public School
Ross Hill Public School
Rouse Hill Public School
Rowland Hassall School
Royal Far West School
Rozelle Public School
Rukenvale Public School
Ruse Public School
Russell Lea Public School
Rydalmere East Public School
Rydalmere Public School
Ryde East Public School
Ryde Public School
Ryde Secondary College"""

s_schools_raw = """Sackville Street Public School
Sadleir Public School
St Andrews Public School
St Clair High School
St Clair Public School
St George Girls' High School
St Georges Basin Public School
St Ives High School
St Ives North Public School
St Ives Park Public School
St Ives Public School
St Johns Park High School
St Johns Park Public School
St Marys North Public School
St Marys Public School
St Marys Senior High School
St Marys South Public School
St. Peters Public School
Samuel Gilbert Public School
Samuel Terry Public School
Sans Souci Public School
Sarah Redfern High School
Sarah Redfern Public School
Schofields Public School
Seaforth Public School
Sefton High School
Seven Hills High School
Seven Hills North Public School
Seven Hills Public School
Seven Hills West Public School
Shalvey Public School
Shelley Public School
Sherwood Grange Public School
Sherwood Ridge Public School
Sir Eric Woodward Memorial School
Sir Joseph Banks High School
Smithfield Public School
Smithfield West Public School
South Coogee Public School
South Sydney High School
Spring Farm Public School
Stanmore Public School
Strathfield Girls High School
Strathfield North Public School
Strathfield South High School
Strathfield South Public School
Summer Hill Public School
Sunning Hill School
Surveyors Creek Public School
Sutherland North Public School
Sutherland Public School
Sydney Boys High School
Sydney Girls High School
Sydney Secondary College
Sydney Japanese International School
Sydney Technical High School
Sylvania Heights Public School
Sylvania High School
Sylvania Public School"""

t_schools_raw = """Telopea Public School
Tempe High School
Tempe Public School
Terrey Hills Public School
Tharawal Public School
Tharbogang Public School
The Forest High School
The Grange Public School
The Hills School (Special School)
The Hills Sports High School
The Jannali High School
The Meadows Public School
The Ponds High School
The Ponds School
Thomas Acres Public School
Thomas Reddall High School
Thornleigh West Public School
Toongabbie East Public School
Toongabbie Public School
Toongabbie West Public School
Tower Street Public School
Tregear Public School
Truscott Street Public School
Turramurra High School
Turramurra North Public School
Turramurra Public School"""

u_schools_raw = """Undercliffe Public School
Upper Lansdowne Public School"""

v_schools_raw = """Vardys Road Public School
Vaucluse Public School
Verona School
Victoria Avenue Public School
Villawood East Public School
Villawood North Public School
Vineyard Public School"""

w_schools_raw = """Wahroonga Public School
Wairoa School (Special School)
Waitara Public School
Wakehurst Public School
Wallacia Public School
Walters Road Public School
Wangee Park School (Special School)
Warwick Farm Public School
Wattawa Heights Public School(
Wattle Grove Public School
Wauchope High School
Wauchope Public School
Waverley Public School
Wentworth Point Public School
Wentworthville Public School
Werrington County Public School
Werrington Public School
West Pennant Hills Public School
West Pymble Public School
West Ryde Public School
Westfields Sports High School
Westmead Public School
Whalan Public School
Widemere Public School
Wideview Public School
Wilberforce Public School
Wiley Park Girls High School
Wiley Park Public School
William Dean Public School
William Rose School (Special School)
William Stimson Public School
Windsor High School
Windsor Park Public School
Windsor Public School
Windsor South Public School
Winston Heights Public School
Winston Hills Public School
Woniora Road School (Special School)
Woodland Road Public School
Woollahra Public School
Woolomin Public School
Woolooware High School
Woolooware Public School
Wyndham College"""

y_schools_raw = """Yagoona Public School
Yarrawarrah Public School
Yates Avenue Public School
Yennora Public School
York Public School"""

for school in y_schools_raw.split("\n"):
    if "Public" in school:
        name = "".join(school.split("Public")[0].strip().split()).lower()
    elif "High" in school:
        name = "".join(school.split("High")[0].strip().split()).lower()
    else:
        name = school.split()[0].lower()
    suffix = ".school@det.nsw.edu.au"
    school_type = "p" if "Public" in school else "h"
    email = name[:10] + "-" + school_type + suffix
    print(school + "\t" + email)
