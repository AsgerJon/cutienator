//  Written by hand on 2026-11-25 from
//  QtAxServer/6.12.0/QtAxServer/private/qclassfactory_p.h, Qt 6.12.0,
//  from Qt's source. Kept as it is when the generator runs again.
//  Qt builds ActiveQt for Windows only. AxServer is a static library,
//  all of it compiled into ours, so the class is taken as exported.
//  What Windows has, as its interfaces and structs, is passed as an
//  address, a 'CLSID' and a 'REFIID' as the address of their
//  'GUID'; a 'DWORD' as an 'unsigned long', a 'BOOL' as an
//  'int', and the 'HRESULT' given back as a 'long'.
//  Not written: 'CreateInstanceLic', taking a 'BSTR', text of
//  Windows (a 'wchar_t *') no row has a word for;
//  'cleanupCreatedApplication', taking a 'QCoreApplication &';
//  the members 'className', 'licensed' and 'classKey', which are
//  no functions; and the template 'QtPrivate::QComObjectTraits' as
//  the same header makes it for 'IClassFactory2'.
#include <QtCore/qglobal.h>
#if defined(Q_OS_WIN)
#include <QtAxServer/6.12.0/QtAxServer/private/qclassfactory_p.h>
#include <cstring>

//  A QClassFactory that Python can take functions over in. Every
//  QClassFactory Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef HRESULT (*CuteQClassFactoryCall0)(const void *, IUnknown *, const IID *, void **, int *);
typedef HRESULT (*CuteQClassFactoryCall1)(const void *, BOOL, int *);
typedef HRESULT (*CuteQClassFactoryCall2)(const void *, DWORD, BSTR *, int *);
typedef HRESULT (*CuteQClassFactoryCall3)(const void *, LICINFO *, int *);
typedef HRESULT (*CuteQClassFactoryCall4)(const void *, const IID *, void **, int *);
typedef ULONG (*CuteQClassFactoryCall5)(const void *, int *);
typedef ULONG (*CuteQClassFactoryCall6)(const void *, int *);
class CuteQClassFactory : public QClassFactory {
public:
  using QClassFactory::QClassFactory;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13IClassFactory14CreateInstanceEP8IUnknownRK5_GUIDPPv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13IClassFactory10LockServerEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14IClassFactory213RequestLicKeyEmPPw")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14IClassFactory210GetLicInfoEP10tagLICINFO")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8IUnknown14QueryInterfaceERK5_GUIDPPv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8IUnknown6AddRefEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8IUnknown7ReleaseEv")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  HRESULT QClassFactory::CreateInstance(IUnknown *pUnkOuter, REFIID iid,
  //      void **ppObject)
  HRESULT STDMETHODCALLTYPE CreateInstance(IUnknown *pUnkOuter, REFIID iid, void **ppObject) override {
    if (taken[0]) {
      int handled = 0;
      CuteQClassFactoryCall0 call = reinterpret_cast<CuteQClassFactoryCall0>(taken[0]);
      HRESULT given = call(this, pUnkOuter, &iid, ppObject, &handled);
      if (handled) return given;
    }
    return QClassFactory::CreateInstance(pUnkOuter, iid, ppObject);
  }

  //  HRESULT QClassFactory::LockServer(BOOL fLock)
  HRESULT STDMETHODCALLTYPE LockServer(BOOL fLock) override {
    if (taken[1]) {
      int handled = 0;
      CuteQClassFactoryCall1 call = reinterpret_cast<CuteQClassFactoryCall1>(taken[1]);
      HRESULT given = call(this, fLock, &handled);
      if (handled) return given;
    }
    return QClassFactory::LockServer(fLock);
  }

  //  HRESULT QClassFactory::RequestLicKey(DWORD a0, BSTR *pKey)
  HRESULT STDMETHODCALLTYPE RequestLicKey(DWORD a0, BSTR *pKey) override {
    if (taken[2]) {
      int handled = 0;
      CuteQClassFactoryCall2 call = reinterpret_cast<CuteQClassFactoryCall2>(taken[2]);
      HRESULT given = call(this, a0, pKey, &handled);
      if (handled) return given;
    }
    return QClassFactory::RequestLicKey(a0, pKey);
  }

  //  HRESULT QClassFactory::GetLicInfo(LICINFO *pLicInfo)
  HRESULT STDMETHODCALLTYPE GetLicInfo(LICINFO *pLicInfo) override {
    if (taken[3]) {
      int handled = 0;
      CuteQClassFactoryCall3 call = reinterpret_cast<CuteQClassFactoryCall3>(taken[3]);
      HRESULT given = call(this, pLicInfo, &handled);
      if (handled) return given;
    }
    return QClassFactory::GetLicInfo(pLicInfo);
  }

  //  HRESULT QComObject<IClassFactory2>::QueryInterface(REFIID riid, void
  //      **ppvObject)
  HRESULT STDMETHODCALLTYPE QueryInterface(REFIID riid, void **ppvObject) override {
    if (taken[4]) {
      int handled = 0;
      CuteQClassFactoryCall4 call = reinterpret_cast<CuteQClassFactoryCall4>(taken[4]);
      HRESULT given = call(this, &riid, ppvObject, &handled);
      if (handled) return given;
    }
    return QComObject<IClassFactory2>::QueryInterface(riid, ppvObject);
  }

  //  ULONG QComObject<IClassFactory2>::AddRef()
  ULONG STDMETHODCALLTYPE AddRef() override {
    if (taken[5]) {
      int handled = 0;
      CuteQClassFactoryCall5 call = reinterpret_cast<CuteQClassFactoryCall5>(taken[5]);
      ULONG given = call(this, &handled);
      if (handled) return given;
    }
    return QComObject<IClassFactory2>::AddRef();
  }

  //  ULONG QComObject<IClassFactory2>::Release()
  ULONG STDMETHODCALLTYPE Release() override {
    if (taken[6]) {
      int handled = 0;
      CuteQClassFactoryCall6 call = reinterpret_cast<CuteQClassFactoryCall6>(taken[6]);
      ULONG given = call(this, &handled);
      if (handled) return given;
    }
    return QComObject<IClassFactory2>::Release();
  }
};

//  QClassFactory::QClassFactory(CLSID clsid)
extern "C" Q_DECL_EXPORT
QClassFactory *ritual_ZN13QClassFactoryC1E5_GUID(const CLSID *clsid) {
  return new CuteQClassFactory(*clsid);
}

//  QClassFactory::~QClassFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QClassFactoryD1Ev(QClassFactory *self) {
  delete self;
}

//  HRESULT QClassFactory::CreateInstanceHelper(IUnknown *pUnkOuter, REFIID
//      iid, void **ppObject)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QClassFactory20CreateInstanceHelperEP8IUnknownRK5_GUIDPPv(
    QClassFactory *self,
    IUnknown *pUnkOuter,
    const IID *iid,
    void **ppObject) {
  return self->CreateInstanceHelper(pUnkOuter, *iid, ppObject);
}

//  HRESULT QClassFactory::CreateInstance(IUnknown *pUnkOuter, REFIID iid,
//      void **ppObject)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QClassFactory14CreateInstanceEP8IUnknownRK5_GUIDPPv(
    QClassFactory *self,
    IUnknown *pUnkOuter,
    const IID *iid,
    void **ppObject) {
  return self->CreateInstance(pUnkOuter, *iid, ppObject);
}

//  HRESULT QClassFactory::LockServer(BOOL fLock)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QClassFactory10LockServerEi(
    QClassFactory *self,
    BOOL fLock) {
  return self->LockServer(fLock);
}

//  HRESULT QClassFactory::RequestLicKey(DWORD a0, BSTR *pKey)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QClassFactory13RequestLicKeyEmPPw(
    QClassFactory *self,
    DWORD a0,
    BSTR *pKey) {
  return self->RequestLicKey(a0, pKey);
}

//  HRESULT QClassFactory::GetLicInfo(LICINFO *pLicInfo)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN13QClassFactory10GetLicInfoEP10tagLICINFO(
    QClassFactory *self,
    LICINFO *pLicInfo) {
  return self->GetLicInfo(pLicInfo);
}

//  a Python function taken by a CuteQClassFactory, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QClassFactory(
    QClassFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQClassFactory *>(self)->take(key, call);
}

//  HRESULT QClassFactory::CreateInstance(IUnknown *pUnkOuter, REFIID iid,
//      void **ppObject)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QClassFactory14CreateInstanceEP8IUnknownRK5_GUIDPPv(
    QClassFactory *self,
    IUnknown *pUnkOuter,
    const IID *iid,
    void **ppObject) {
  return self->QClassFactory::CreateInstance(pUnkOuter, *iid, ppObject);
}

//  HRESULT QClassFactory::LockServer(BOOL fLock)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QClassFactory10LockServerEi(
    QClassFactory *self,
    BOOL fLock) {
  return self->QClassFactory::LockServer(fLock);
}

//  HRESULT QClassFactory::RequestLicKey(DWORD a0, BSTR *pKey)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QClassFactory13RequestLicKeyEmPPw(
    QClassFactory *self,
    DWORD a0,
    BSTR *pKey) {
  return self->QClassFactory::RequestLicKey(a0, pKey);
}

//  HRESULT QClassFactory::GetLicInfo(LICINFO *pLicInfo)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN13QClassFactory10GetLicInfoEP10tagLICINFO(
    QClassFactory *self,
    LICINFO *pLicInfo) {
  return self->QClassFactory::GetLicInfo(pLicInfo);
}

#endif  // defined(Q_OS_WIN)
