"""Stream type classes for tap-cin7."""

from singer_sdk import typing as th

from tap_cin7.client import CIN7Stream


class ProductStream(CIN7Stream):
    """Define custom stream."""

    name = "products"
    path = "/v1/Products?rows=250"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$[*]"
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("status", th.StringType),
        th.Property("createdDate", th.StringType),
        th.Property("modifiedDate", th.StringType),
        th.Property("description", th.StringType),
        th.Property(
            "images", th.ArrayType(th.ObjectType(th.Property("link", th.StringType)))
        ),
        th.Property("supplierId", th.IntegerType),
        th.Property("brand", th.StringType),
        th.Property("category", th.StringType),
        th.Property("stockControl", th.IntegerType),
        th.Property("orderType", th.StringType),
        th.Property("productType", th.StringType),
        th.Property(
            "productOptions",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("createdDate", th.StringType),
                    th.Property("modifiedDate", th.StringType),
                    th.Property("status", th.StringType),
                    th.Property("productId", th.IntegerType),
                    th.Property("code", th.StringType),
                    th.Property("barcode", th.StringType),
                    th.Property("retailPrice", th.NumberType),
                    th.Property("wholesalePrice", th.NumberType),
                    th.Property("vipPrice", th.NumberType),
                    th.Property("specialPrice", th.NumberType),
                    th.Property("specialsStartDate", th.StringType),
                    th.Property("specialDays", th.IntegerType),
                    th.Property("stockAvailable", th.NumberType),
                    th.Property("stockOnHand", th.NumberType),
                    th.Property(
                        "image", th.ObjectType(th.Property("link", th.StringType))
                    ),
                    th.Property(
                        "priceColumns",
                        th.ObjectType(
                            th.Property("priceAUD", th.NumberType),
                            th.Property("priceGBP", th.NumberType),
                            th.Property("costNZD", th.NumberType),
                        ),
                    ),
                )
            ),
        ),
    ).to_dict()


class PurchaseOrdersStream(CIN7Stream):
    """Define custom stream."""

    name = "purchase_orders"
    path = "/v1/PurchaseOrders?rows=250"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$[*]"
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("createdDate", th.StringType),
        th.Property("modifiedDate", th.StringType),
        th.Property("createdBy", th.IntegerType),
        th.Property("processedBy", th.IntegerType),
        th.Property("isApproved", th.BooleanType),
        th.Property("reference", th.StringType),
        th.Property("memberId", th.IntegerType),
        th.Property("firstName", th.StringType),
        th.Property("lastName", th.StringType),
        th.Property("company", th.StringType),
        th.Property("email", th.StringType),
        th.Property("phone", th.StringType),
        th.Property("mobile", th.StringType),
        th.Property("fax", th.StringType),
        th.Property("deliveryFirstName", th.StringType),
        th.Property("deliveryLastName", th.StringType),
        th.Property("deliveryCompany", th.StringType),
        th.Property("deliveryAddress1", th.StringType),
        th.Property("deliveryAddress2", th.StringType),
        th.Property("deliveryCity", th.StringType),
        th.Property("deliveryState", th.StringType),
        th.Property("deliveryPostalCode", th.StringType),
        th.Property("deliveryCountry", th.StringType),
        th.Property("billingFirstName", th.StringType),
        th.Property("billingLastName", th.StringType),
        th.Property("billingCompany", th.StringType),
        th.Property("billingAddress1", th.StringType),
        th.Property("billingAddress2", th.StringType),
        th.Property("billingCity", th.StringType),
        th.Property("billingPostalCode", th.StringType),
        th.Property("billingState", th.StringType),
        th.Property("billingCountry", th.StringType),
        th.Property("branchId", th.IntegerType),
        th.Property("branchEmail", th.StringType),
        th.Property("projectName", th.StringType),
        th.Property("trackingCode", th.StringType),
        th.Property("internalComments", th.StringType),
        th.Property("productTotal", th.NumberType),
        th.Property("freightTotal", th.NumberType),
        th.Property("freightDescription", th.StringType),
        th.Property("surcharge", th.NumberType),
        th.Property("surchargeDescription", th.StringType),
        th.Property("discountTotal", th.NumberType),
        th.Property("discountDescription", th.StringType),
        th.Property("total", th.NumberType),
        th.Property("currencyCode", th.StringType),
        th.Property("currencyRate", th.NumberType),
        th.Property("currencySymbol", th.StringType),
        th.Property("taxStatus", th.StringType),
        th.Property("taxRate", th.NumberType),
        th.Property("source", th.StringType),
        th.Property("isVoid", th.BooleanType),
        th.Property("memberEmail", th.StringType),
        th.Property("memberCostCenter", th.StringType),
        th.Property("memberAlternativeTaxRate", th.StringType),
        th.Property("costCenter", th.StringType),
        th.Property("alternativeTaxRate", th.StringType),
        th.Property("estimatedDeliveryDate", th.StringType),
        th.Property("salesPersonId", th.NumberType),
        th.Property("salesPersonEmail", th.StringType),
        th.Property("paymentTerms", th.StringType),
        th.Property("customerOrderNo", th.StringType),
        th.Property("voucherCode", th.StringType),
        th.Property("deliveryInstructions", th.StringType),
        th.Property("status", th.StringType),
        th.Property("stage", th.StringType),
        th.Property("supplierInvoiceReference", th.StringType),
        th.Property("supplierAcceptanceDate", th.StringType),
        th.Property("fullyReceivedDate", th.StringType),
        th.Property("invoiceDate", th.StringType),
        th.Property(
            "lineItems",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("createdDate", th.StringType),
                    th.Property("transactionId", th.IntegerType),
                    th.Property("parentId", th.IntegerType),
                    th.Property("productId", th.IntegerType),
                    th.Property("productOptionId", th.IntegerType),
                    th.Property("integrationRef", th.StringType),
                    th.Property("sort", th.IntegerType),
                    th.Property("code", th.StringType),
                    th.Property("name", th.StringType),
                    th.Property("option1", th.StringType),
                    th.Property("option2", th.StringType),
                    th.Property("option3", th.StringType),
                    th.Property("qty", th.NumberType),
                    th.Property("styleCode", th.StringType),
                    th.Property("barcode", th.StringType),
                    th.Property("sizeCodes", th.StringType),
                    th.Property("lineComments", th.StringType),
                    th.Property("unitPrice", th.NumberType),
                    th.Property("discount", th.NumberType),
                    th.Property("qtyShipped", th.NumberType),
                    th.Property("holdingQty", th.NumberType),
                    th.Property("accountCode", th.StringType),
                )
            ),
            th.Property("logisticsCarrier", th.StringType),
            th.Property("logisticsCarrier", th.IntegerType),
        ),
    ).to_dict()


class OrderStream(CIN7Stream):
    """Define custom stream."""

    name = "sale_order"
    path = "/v1/SalesOrders?rows=250"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$[*]"
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("createdDate", th.StringType),
        th.Property("modifiedDate", th.StringType),
        th.Property("createdBy", th.IntegerType),
        th.Property("processedBy", th.IntegerType),
        th.Property("isApproved", th.BooleanType),
        th.Property("reference", th.StringType),
        th.Property("memberId", th.IntegerType),
        th.Property("firstName", th.StringType),
        th.Property("lastName", th.StringType),
        th.Property("company", th.StringType),
        th.Property("email", th.StringType),
        th.Property("phone", th.StringType),
        th.Property("mobile", th.StringType),
        th.Property("fax", th.StringType),
        th.Property("deliveryFirstName", th.StringType),
        th.Property("deliveryLastName", th.StringType),
        th.Property("deliveryCompany", th.StringType),
        th.Property("deliveryAddress1", th.StringType),
        th.Property("deliveryAddress2", th.StringType),
        th.Property("deliveryCity", th.StringType),
        th.Property("deliveryState", th.StringType),
        th.Property("deliveryPostalCode", th.StringType),
        th.Property("deliveryCountry", th.StringType),
        th.Property("billingFirstName", th.StringType),
        th.Property("billingLastName", th.StringType),
        th.Property("billingCompany", th.StringType),
        th.Property("billingAddress1", th.StringType),
        th.Property("billingAddress2", th.StringType),
        th.Property("billingCity", th.StringType),
        th.Property("billingPostalCode", th.StringType),
        th.Property("billingState", th.StringType),
        th.Property("billingCountry", th.StringType),
        th.Property("branchId", th.IntegerType),
        th.Property("branchEmail", th.StringType),
        th.Property("projectName", th.StringType),
        th.Property("trackingCode", th.StringType),
        th.Property("internalComments", th.StringType),
        th.Property("productTotal", th.NumberType),
        th.Property("freightTotal", th.NumberType),
        th.Property("freightDescription", th.StringType),
        th.Property("surcharge", th.NumberType),
        th.Property("surchargeDescription", th.StringType),
        th.Property("discountTotal", th.NumberType),
        th.Property("discountDescription", th.StringType),
        th.Property("total", th.NumberType),
        th.Property("currencyCode", th.StringType),
        th.Property("currencyRate", th.NumberType),
        th.Property("currencySymbol", th.StringType),
        th.Property("taxStatus", th.StringType),
        th.Property("taxRate", th.NumberType),
        th.Property("source", th.StringType),
        th.Property("isVoid", th.BooleanType),
        th.Property("memberEmail", th.StringType),
        th.Property("memberCostCenter", th.StringType),
        th.Property("memberAlternativeTaxRate", th.StringType),
        th.Property("costCenter", th.StringType),
        th.Property("alternativeTaxRate", th.StringType),
        th.Property("estimatedDeliveryDate", th.StringType),
        th.Property("salesPersonId", th.NumberType),
        th.Property("salesPersonEmail", th.StringType),
        th.Property("paymentTerms", th.StringType),
        th.Property("customerOrderNo", th.StringType),
        th.Property("voucherCode", th.StringType),
        th.Property("deliveryInstructions", th.StringType),
        th.Property("status", th.StringType),
        th.Property("stage", th.StringType),
        th.Property("invoiceDate", th.StringType),
        th.Property("invoiceNumber", th.IntegerType),
        th.Property("dispatchedDate", th.StringType),
        th.Property("logisticsCarrier", th.StringType),
        th.Property("logisticsStatus", th.IntegerType),
        th.Property("distributionBranchId", th.IntegerType),
        th.Property(
            "lineItems",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("createdDate", th.StringType),
                    th.Property("transactionId", th.IntegerType),
                    th.Property("parentId", th.IntegerType),
                    th.Property("productId", th.IntegerType),
                    th.Property("productOptionId", th.IntegerType),
                    th.Property("integrationRef", th.StringType),
                    th.Property("sort", th.IntegerType),
                    th.Property("code", th.StringType),
                    th.Property("name", th.StringType),
                    th.Property("option1", th.StringType),
                    th.Property("option2", th.StringType),
                    th.Property("option3", th.StringType),
                    th.Property("qty", th.NumberType),
                    th.Property("styleCode", th.StringType),
                    th.Property("barcode", th.StringType),
                    th.Property("sizeCodes", th.StringType),
                    th.Property("lineComments", th.StringType),
                    th.Property("unitPrice", th.NumberType),
                    th.Property("discount", th.NumberType),
                    th.Property("qtyShipped", th.NumberType),
                    th.Property("holdingQty", th.NumberType),
                    th.Property("accountCode", th.StringType),
                    th.Property("stockControl", th.StringType),
                    # th.Property("stockMovements", th.StringType),
                    # th.Property("sizes", th.StringType)
                )
            ),
        ),
    ).to_dict()


class StockStream(CIN7Stream):
    """Define custom stream."""

    name = "stockstream"
    path = "/v1/Stock?rows=250"
    primary_keys = ["productId"]
    replication_key = None
    records_jsonpath = "$[*]"

    schema = th.PropertiesList(
        th.Property("productId", th.IntegerType),
        th.Property("productOptionId", th.IntegerType),
        th.Property("modifiedDate", th.StringType),
        th.Property("styleCode", th.StringType),
        th.Property("code", th.StringType),
        th.Property("barcode", th.StringType),
        th.Property("branchId", th.IntegerType),
        th.Property("branchName", th.StringType),
        th.Property("productName", th.StringType),
        th.Property("option1", th.StringType),
        th.Property("option2", th.StringType),
        th.Property("option3", th.StringType),
        th.Property("size", th.StringType),
        th.Property("available", th.NumberType),
        th.Property("stockOnHand", th.NumberType),
        th.Property("openSales", th.NumberType),
        th.Property("incoming", th.NumberType),
        th.Property("virtual", th.NumberType),
        th.Property("holding", th.NumberType),
    ).to_dict()


class VoucherStream(CIN7Stream):
    """Define custom stream."""

    name = "voucher"
    path = "/v1/Voucher?rows=250"
    primary_keys = ["customerID"]
    replication_key = None
    records_jsonpath = "$[*]"
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property("customerID", th.IntegerType),
        th.Property("createdDate", th.StringType),
        th.Property("status", th.StringType),
        th.Property("code", th.StringType),
        th.Property("type", th.StringType),
        th.Property("description", th.StringType),
        th.Property("expiryDate", th.StringType),
        th.Property("amount", th.NumberType),
        th.Property("customerEmail", th.StringType),
        th.Property("redeemedCount", th.IntegerType),
        th.Property("redeemedCountLimit", th.IntegerType),
        th.Property("redeemedAmount", th.NumberType),
    ).to_dict()


class ContactsStream(CIN7Stream):
    """Define custom stream."""

    name = "contact_supplier"
    path = "/v1/Contacts?where=type='Supplier'&rows=250"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$[*]"
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("createdDate", th.StringType),
        th.Property("modifiedDate", th.StringType),
        th.Property("isActive", th.BooleanType),
        th.Property("type", th.StringType),
        th.Property("company", th.StringType),
        th.Property("firstName", th.StringType),
        th.Property("lastName", th.StringType),
        th.Property("jobTitle", th.StringType),
        th.Property("email", th.StringType),
        th.Property("website", th.StringType),
        th.Property("phone", th.StringType),
        th.Property("fax", th.StringType),
        th.Property("mobile", th.StringType),
        th.Property("address1", th.StringType),
        th.Property("address2", th.StringType),
        th.Property("city", th.StringType),
        th.Property("state", th.StringType),
        th.Property("postCode", th.StringType),
        th.Property("country", th.StringType),
        th.Property("postalAddress1", th.StringType),
        th.Property("postalAddress2", th.StringType),
        th.Property("postalCity", th.StringType),
        th.Property("postalPostCode", th.StringType),
        th.Property("postalState", th.StringType),
        th.Property("postalCountry", th.StringType),
        th.Property("notes", th.StringType),
        th.Property("integrationRef", th.StringType),
        th.Property("salesPersonId", th.IntegerType),
        th.Property("accountNumber", th.StringType),
        th.Property("billingId", th.IntegerType),
        th.Property("billingCompany", th.StringType),
        th.Property("accountsFirstName", th.StringType),
        th.Property("accountsLastName", th.StringType),
        th.Property("billingEmail", th.StringType),
        th.Property("accountsPhone", th.StringType),
        th.Property("billingCostCenter", th.StringType),
        th.Property("priceColumn", th.StringType),
        th.Property("creditLimit", th.NumberType),
        th.Property("balanceOwing", th.NumberType),
    ).to_dict()


class BranchesStream(CIN7Stream):
    """Define custom stream."""

    name = "branches"
    path = "/v1/Branches"
    primary_keys = ["Id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.NumberType),
        th.Property("branchType", th.StringType),
        th.Property("stockControlOptions", th.StringType),
        th.Property("taxStatus", th.StringType),
        th.Property("accountNumber", th.StringType),
        th.Property(
            "branchLocations",
            th.ArrayType(
                th.ObjectType(
                    th.Property("zone", th.StringType),
                    th.Property("bins", th.CustomType({"type": ["array", "string"]})),
                )
            ),
        ),
        th.Property("createdDate", th.DateTimeType),
        th.Property("modifiedDate", th.DateTimeType),
        th.Property("isActive", th.BooleanType),
        th.Property("company", th.StringType),
        th.Property("firstName", th.StringType),
        th.Property("lastName", th.StringType),
        th.Property("jobTitle", th.StringType),
        th.Property("email", th.StringType),
        th.Property("website", th.StringType),
        th.Property("phone", th.StringType),
        th.Property("fax", th.StringType),
        th.Property("mobile", th.StringType),
        th.Property("address1", th.StringType),
        th.Property("address2", th.StringType),
        th.Property("city", th.StringType),
        th.Property("state", th.StringType),
        th.Property("postCode", th.StringType),
        th.Property("country", th.StringType),
        th.Property("postalAddress1", th.StringType),
        th.Property("postalAddress2", th.StringType),
        th.Property("postalCity", th.StringType),
        th.Property("postalPostCode", th.StringType),
        th.Property("postalState", th.StringType),
        th.Property("postalCountry", th.StringType),
        th.Property("notes", th.StringType),
        th.Property("integrationRef", th.StringType),
        th.Property("customFields", th.CustomType({"type": ["object", "string"]})),
        th.Property(
            "secondaryContacts",
            th.ArrayType(
                th.ObjectType(
                    th.Property("Id", th.NumberType),
                    th.Property("Company", th.StringType),
                    th.Property("FirstName", th.StringType),
                    th.Property("LastName", th.StringType),
                    th.Property("JobTitle", th.StringType),
                    th.Property("Email", th.StringType),
                    th.Property("Mobile", th.StringType),
                    th.Property("Phone", th.StringType),
                )
            ),
        ),
    ).to_dict()
