def form_input(driver, id_val, submit=None):
    for field_id in id_val:
        field = driver.find_element_by_id(field_id)
        field.send_keys(id_val[field_id])
    if submit:
        driver.find_element_by_id(submit).click()
