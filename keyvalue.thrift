
struct GetRequest {
    1: string key
}

struct SetRequest {
    1: string key,
    2: string val,
    3: i64 ttl = 0
}

struct GetResponse {
    1: string val
}

exception KeyNotFound {

}

service KeyValueService {
    GetResponse Get(1:GetRequest req) throws(1:KeyNotFound ex),
    void Set(1:SetRequest req)
}