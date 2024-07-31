import requests
from bs4 import BeautifulSoup
import json


if __name__ == "__main__":

    url = (
        "https://ofsistorage.blob.core.windows.net/publishlive/2022format/ConList.html"
    )
    response = requests.get(url)

    financial_target_list = []

    soup = BeautifulSoup(response.content, "html.parser")

    page = soup.find("body")

    h1_tags = page.find_all("h1")

    for tag in h1_tags:
        target_dict = {}
        if tag.find("u"):
            target_dict[tag.find("u").text.strip()] = tag.text.strip("REGIME: ")
            individual_tag = tag.find_next_sibling(
                "h2", string="INDIVIDUALS"
            ).find_next_sibling("ol")
            li_tags = individual_tag.find_all("li", class_="SpacedOut")

            individual_list = []
            for item in li_tags:
                individual_dict = {}

                name_tag = (
                    item.find("b", string="Name 6:")
                    if item.find("b", string="Name 6:")
                    else None
                )
                if name_tag:
                    individual_dict["Name"] = name_tag.find_next_sibling(
                        string=True
                    ).strip()

                second_name_tag = (
                    item.find("b", string="1:") if item.find("b", string="1:") else None
                )
                if second_name_tag:
                    individual_dict["Second Name"] = second_name_tag.find_next_sibling(
                        string=True
                    ).strip()

                position_tag = (
                    item.find("b", string="Position:")
                    if item.find("b", string="Position:")
                    else None
                )
                if position_tag:
                    individual_dict["Position"] = position_tag.find_next_sibling(
                        string=True
                    ).strip()

                dob_tag = (
                    item.find("b", string="DOB:")
                    if item.find("b", string="DOB:")
                    else None
                )
                if dob_tag:
                    individual_dict["DOB"] = dob_tag.find_next_sibling(
                        string=True
                    ).strip()

                pob_tag = (
                    item.find("b", string="POB:")
                    if item.find("b", string="POB:")
                    else None
                )
                if pob_tag:
                    individual_dict["POB"] = pob_tag.find_next_sibling(
                        string=True
                    ).strip()

                address_tag = (
                    item.find("b", string="Address:")
                    if item.find("b", string="Address:")
                    else None
                )
                if address_tag:
                    individual_dict["Address"] = address_tag.find_next_sibling(
                        string=True
                    ).strip()

                aka_tag = (
                    item.find("b", string="Good quality a.k.a:")
                    if item.find("b", string="Good quality a.k.a:")
                    else None
                )
                if aka_tag:
                    individual_dict["Good quality a.k.a"] = aka_tag.find_next_sibling(
                        string=True
                    ).strip()
                passport_no_tag = (
                    item.find("b", string="Passport Number:")
                    if item.find("b", string="Passport Number:")
                    else None
                )

                if passport_no_tag:
                    individual_dict["Passport Number"] = (
                        passport_no_tag.find_next_sibling(string=True).strip()
                    )

                passport_detail_tag = (
                    item.find("b", string="Passport Details:")
                    if item.find("b", string="Passport Details:")
                    else None
                )
                if passport_detail_tag:
                    individual_dict["Passport Details"] = (
                        passport_detail_tag.find_next_sibling(string=True).strip()
                    )

                nin_tag = (
                    item.find("b", string="National Identification Number:")
                    if item.find("b", string="National Identification Number:")
                    else None
                )
                if nin_tag:
                    individual_dict["National Identification Number"] = (
                        nin_tag.find_next_sibling(string=True).strip()
                    )

                nid_tag = (
                    item.find("b", string="National Identification Details:")
                    if item.find("b", string="National Identification Details:")
                    else None
                )
                if nid_tag:
                    individual_dict["National Identification Details"] = (
                        nid_tag.find_next_sibling(string=True).strip()
                    )

                nationality_tag = (
                    item.find("b", string="Nationality:")
                    if item.find("b", string="Nationality:")
                    else None
                )
                if nationality_tag:
                    individual_dict["Nationality"] = nationality_tag.find_next_sibling(
                        string=True
                    ).strip()

                other_information_tag = (
                    item.find("b", string="Other Information:")
                    if item.find("b", string="Other Information:")
                    else None
                )
                if other_information_tag:
                    individual_dict["Other Information"] = (
                        other_information_tag.find_next_sibling(string=True).strip()
                    )

                listed_on_tag = (
                    item.find("b", string="Listed on:")
                    if item.find("b", string="Listed on:")
                    else None
                )
                if listed_on_tag:
                    individual_dict["Listed on"] = listed_on_tag.find_next_sibling(
                        string=True
                    ).strip()

                sanction_date_tag = (
                    item.find("b", string="UK Sanctions List Date Designated:")
                    if item.find("b", string="UK Sanctions List Date Designated:")
                    else None
                )
                if sanction_date_tag:
                    individual_dict["UK Sanctions List Date Designated"] = (
                        sanction_date_tag.find_next_sibling(string=True).strip()
                    )

                last_update_date_tag = (
                    item.find("b", string="Last Updated:")
                    if item.find("b", string="Last Updated:")
                    else None
                )
                if last_update_date_tag:
                    individual_dict["Last Updated"] = (
                        last_update_date_tag.find_next_sibling(string=True).strip()
                    )

                group_id_tag = (
                    item.find("b", string="Group ID:")
                    if item.find("b", string="Group ID:")
                    else None
                )
                if group_id_tag:
                    individual_dict["Group ID"] = group_id_tag.find_next_sibling(
                        string=True
                    ).strip()

                individual_list.append(individual_dict)
            target_dict["INDIVIDUAL"] = individual_list

            entity_tag = tag.find_next_sibling(
                "h2", string="ENTITIES"
            ).find_next_sibling("ol")
            li_tags = entity_tag.find_all("li", class_="SpacedOut")

            entity_list = []
            for item in li_tags:
                entity_dict = {}

                org_name_tag = (
                    item.find("b", string="Organisation Name:")
                    if item.find("b", string="Organisation Name:")
                    else None
                )
                if org_name_tag:
                    entity_dict["Organisation Name"] = org_name_tag.find_next_sibling(
                        string=True
                    ).strip()

                address_tag = (
                    item.find("b", string="Address:")
                    if item.find("b", string="Address:")
                    else None
                )
                if address_tag:
                    entity_dict["Address"] = address_tag.find_next_sibling(
                        string=True
                    ).strip()

                other_information_tag = (
                    item.find("b", string="Other Information:")
                    if item.find("b", string="Other Information:")
                    else None
                )
                if other_information_tag:
                    individual_dict["Other Information"] = (
                        other_information_tag.find_next_sibling(string=True).strip()
                    )

                listed_on_tag = (
                    item.find("b", string="Listed on:")
                    if item.find("b", string="Listed on:")
                    else None
                )
                if listed_on_tag:
                    entity_dict["Listed on"] = listed_on_tag.find_next_sibling(
                        string=True
                    ).strip()

                sanction_date_tag = (
                    item.find("b", string="UK Sanctions List Date Designated:")
                    if item.find("b", string="UK Sanctions List Date Designated:")
                    else None
                )
                if sanction_date_tag:
                    entity_dict["UK Sanctions List Date Designated"] = (
                        sanction_date_tag.find_next_sibling(string=True).strip()
                    )

                last_update_date_tag = (
                    item.find("b", string="Last Updated:")
                    if item.find("b", string="Last Updated:")
                    else None
                )
                if last_update_date_tag:
                    entity_dict["Last Updated"] = (
                        last_update_date_tag.find_next_sibling(string=True).strip()
                    )

                group_id_tag = (
                    item.find("b", string="Group ID:")
                    if item.find("b", string="Group ID:")
                    else None
                )
                if group_id_tag:
                    entity_dict["Group ID"] = group_id_tag.find_next_sibling(
                        string=True
                    ).strip()

                entity_list.append(entity_dict)
            target_dict["ENTITY"] = individual_list

            financial_target_list.append(target_dict)

    with open("financial_target.json", "w") as json_file:
        json.dump(financial_target_list, json_file, indent=4, ensure_ascii=False)

    print("financial target has been written to financial_target.json")
