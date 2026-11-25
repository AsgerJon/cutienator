//  Written by hand on 2026-11-25 from
//  QtAxServer/6.12.0/QtAxServer/private/qaxsignalvec_p.h, Qt 6.12.0,
//  from Qt's source. Kept as it is when the generator runs again.
//  Qt builds ActiveQt for Windows only. AxServer is a static library,
//  all of it compiled into ours, so the class is taken as exported.
//  What Windows has, as its interfaces, is passed as an address, a
//  'ULONG' as an 'unsigned long', and the 'HRESULT' given back as
//  a 'long'.
//  Not written: the constructor taking a 'ConnectionPoints', a QMap;
//  the move constructor and 'operator=', which Qt deletes; and a
//  destructor, which the class declares not: 'Release' deletes it.
#include <QtCore/qglobal.h>
#if defined(Q_OS_WIN)
#include <QtAxServer/6.12.0/QtAxServer/private/qaxsignalvec_p.h>
#include <cstring>

//  A QAxSignalVec that Python can take functions over in. Every
//  QAxSignalVec Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef HRESULT (*CuteQAxSignalVecCall0)(const void *, ULONG, LPCONNECTIONPOINT *, ULONG *, int *);
typedef HRESULT (*CuteQAxSignalVecCall1)(const void *, ULONG, int *);
typedef HRESULT (*CuteQAxSignalVecCall2)(const void *, int *);
typedef HRESULT (*CuteQAxSignalVecCall3)(const void *, IEnumConnectionPoints **, int *);
typedef HRESULT (*CuteQAxSignalVecCall4)(const void *, const IID *, void **, int *);
typedef ULONG (*CuteQAxSignalVecCall5)(const void *, int *);
typedef ULONG (*CuteQAxSignalVecCall6)(const void *, int *);
class CuteQAxSignalVec : public QAxSignalVec {
public:
  using QAxSignalVec::QAxSignalVec;
  CuteQAxSignalVec(const QAxSignalVec &other) : QAxSignalVec(other) {}
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21IEnumConnectionPoints4NextEmPP16IConnectionPointPm")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21IEnumConnectionPoints4SkipEm")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21IEnumConnectionPoints5ResetEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21IEnumConnectionPoints5CloneEPPS_")) {
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

  //  HRESULT QAxSignalVec::Next(ULONG cConnections, LPCONNECTIONPOINT *ppCP,
  //      ULONG *pcFetched)
  HRESULT STDMETHODCALLTYPE Next(ULONG cConnections, LPCONNECTIONPOINT *ppCP, ULONG *pcFetched) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAxSignalVecCall0 call = reinterpret_cast<CuteQAxSignalVecCall0>(taken[0]);
      HRESULT given = call(this, cConnections, ppCP, pcFetched, &handled);
      if (handled) return given;
    }
    return QAxSignalVec::Next(cConnections, ppCP, pcFetched);
  }

  //  HRESULT QAxSignalVec::Skip(ULONG cConnections)
  HRESULT STDMETHODCALLTYPE Skip(ULONG cConnections) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAxSignalVecCall1 call = reinterpret_cast<CuteQAxSignalVecCall1>(taken[1]);
      HRESULT given = call(this, cConnections, &handled);
      if (handled) return given;
    }
    return QAxSignalVec::Skip(cConnections);
  }

  //  HRESULT QAxSignalVec::Reset()
  HRESULT STDMETHODCALLTYPE Reset() override {
    if (taken[2]) {
      int handled = 0;
      CuteQAxSignalVecCall2 call = reinterpret_cast<CuteQAxSignalVecCall2>(taken[2]);
      HRESULT given = call(this, &handled);
      if (handled) return given;
    }
    return QAxSignalVec::Reset();
  }

  //  HRESULT QAxSignalVec::Clone(IEnumConnectionPoints **ppEnum)
  HRESULT STDMETHODCALLTYPE Clone(IEnumConnectionPoints **ppEnum) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAxSignalVecCall3 call = reinterpret_cast<CuteQAxSignalVecCall3>(taken[3]);
      HRESULT given = call(this, ppEnum, &handled);
      if (handled) return given;
    }
    return QAxSignalVec::Clone(ppEnum);
  }

  //  HRESULT QComObject<IEnumConnectionPoints>::QueryInterface(REFIID riid,
  //      void **ppvObject)
  HRESULT STDMETHODCALLTYPE QueryInterface(REFIID riid, void **ppvObject) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAxSignalVecCall4 call = reinterpret_cast<CuteQAxSignalVecCall4>(taken[4]);
      HRESULT given = call(this, &riid, ppvObject, &handled);
      if (handled) return given;
    }
    return QComObject<IEnumConnectionPoints>::QueryInterface(riid, ppvObject);
  }

  //  ULONG QComObject<IEnumConnectionPoints>::AddRef()
  ULONG STDMETHODCALLTYPE AddRef() override {
    if (taken[5]) {
      int handled = 0;
      CuteQAxSignalVecCall5 call = reinterpret_cast<CuteQAxSignalVecCall5>(taken[5]);
      ULONG given = call(this, &handled);
      if (handled) return given;
    }
    return QComObject<IEnumConnectionPoints>::AddRef();
  }

  //  ULONG QComObject<IEnumConnectionPoints>::Release()
  ULONG STDMETHODCALLTYPE Release() override {
    if (taken[6]) {
      int handled = 0;
      CuteQAxSignalVecCall6 call = reinterpret_cast<CuteQAxSignalVecCall6>(taken[6]);
      ULONG given = call(this, &handled);
      if (handled) return given;
    }
    return QComObject<IEnumConnectionPoints>::Release();
  }
};

//  QAxSignalVec::QAxSignalVec(const QAxSignalVec &old)
extern "C" Q_DECL_EXPORT
QAxSignalVec *ritual_ZN12QAxSignalVecC1ERKS_(const QAxSignalVec *old) {
  return new CuteQAxSignalVec(*old);
}

//  HRESULT QAxSignalVec::Next(ULONG cConnections, LPCONNECTIONPOINT *ppCP,
//      ULONG *pcFetched)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN12QAxSignalVec4NextEmPP16IConnectionPointPm(
    QAxSignalVec *self,
    ULONG cConnections,
    LPCONNECTIONPOINT *ppCP,
    ULONG *pcFetched) {
  return self->Next(cConnections, ppCP, pcFetched);
}

//  HRESULT QAxSignalVec::Skip(ULONG cConnections)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN12QAxSignalVec4SkipEm(
    QAxSignalVec *self,
    ULONG cConnections) {
  return self->Skip(cConnections);
}

//  HRESULT QAxSignalVec::Reset()
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN12QAxSignalVec5ResetEv(QAxSignalVec *self) {
  return self->Reset();
}

//  HRESULT QAxSignalVec::Clone(IEnumConnectionPoints **ppEnum)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN12QAxSignalVec5CloneEPP21IEnumConnectionPoints(
    QAxSignalVec *self,
    IEnumConnectionPoints **ppEnum) {
  return self->Clone(ppEnum);
}

//  a Python function taken by a CuteQAxSignalVec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAxSignalVec(
    QAxSignalVec *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAxSignalVec *>(self)->take(key, call);
}

//  HRESULT QAxSignalVec::Next(ULONG cConnections, LPCONNECTIONPOINT *ppCP,
//      ULONG *pcFetched)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN12QAxSignalVec4NextEmPP16IConnectionPointPm(
    QAxSignalVec *self,
    ULONG cConnections,
    LPCONNECTIONPOINT *ppCP,
    ULONG *pcFetched) {
  return self->QAxSignalVec::Next(cConnections, ppCP, pcFetched);
}

//  HRESULT QAxSignalVec::Skip(ULONG cConnections)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN12QAxSignalVec4SkipEm(
    QAxSignalVec *self,
    ULONG cConnections) {
  return self->QAxSignalVec::Skip(cConnections);
}

//  HRESULT QAxSignalVec::Reset()
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN12QAxSignalVec5ResetEv(QAxSignalVec *self) {
  return self->QAxSignalVec::Reset();
}

//  HRESULT QAxSignalVec::Clone(IEnumConnectionPoints **ppEnum)
extern "C" Q_DECL_EXPORT
HRESULT ritual_own_ZN12QAxSignalVec5CloneEPP21IEnumConnectionPoints(
    QAxSignalVec *self,
    IEnumConnectionPoints **ppEnum) {
  return self->QAxSignalVec::Clone(ppEnum);
}

#endif  // defined(Q_OS_WIN)
