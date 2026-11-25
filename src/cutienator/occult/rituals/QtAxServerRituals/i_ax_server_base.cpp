//  Written by hand on 2026-11-25 from
//  QtAxServer/6.12.0/QtAxServer/private/iaxserverbase_p.h, Qt 6.12.0,
//  from Qt's source. Kept as it is when the generator runs again.
//  Qt builds ActiveQt for Windows only. AxServer is a static library,
//  all of it compiled into ours, so the struct is taken as exported.
//  It is an interface of COM: every function of it is pure and is
//  called through the object. An 'HRESULT' is given back as a
//  'long', a 'ULONG' as an 'unsigned long'.
//  Not written: a constructor, as the struct is abstract; a
//  destructor, which it declares not; and the variable
//  'IID_IAxServerBase', which is no function.
#include <QtCore/qglobal.h>
#if defined(Q_OS_WIN)
#include <QtAxServer/6.12.0/QtAxServer/private/iaxserverbase_p.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A IAxServerBase that Python can take functions over in. Every
//  IAxServerBase Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef void * (*CuteIAxServerBaseCall0)(const void *, int *);
typedef void (*CuteIAxServerBaseCall1)(const void *, const char *, int *);
typedef bool (*CuteIAxServerBaseCall2)(const void *, const char *, int *);
typedef void * (*CuteIAxServerBaseCall3)(const void *, int *);
typedef void (*CuteIAxServerBaseCall4)(const void *, int, const QString *, const QString *, const QString *, int *);
typedef HRESULT (*CuteIAxServerBaseCall5)(const void *, const IID *, void **, int *);
typedef ULONG (*CuteIAxServerBaseCall6)(const void *, int *);
typedef ULONG (*CuteIAxServerBaseCall7)(const void *, int *);
class CuteIAxServerBase : public IAxServerBase {
public:
  using IAxServerBase::IAxServerBase;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13IAxServerBase10ClientSiteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13IAxServerBase19EmitPropertyChangedEPKc")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13IAxServerBase25EmitRequestPropertyChangeEPKc")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13IAxServerBase10GetQObjectEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13IAxServerBase11ReportErrorEiRK7QStringS2_S2_")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8IUnknown14QueryInterfaceERK5_GUIDPPv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8IUnknown6AddRefEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8IUnknown7ReleaseEv")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  IUnknown *IAxServerBase::ClientSite() const
  IUnknown *STDMETHODCALLTYPE ClientSite() const override {
    if (taken[0]) {
      int handled = 0;
      CuteIAxServerBaseCall0 call = reinterpret_cast<CuteIAxServerBaseCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<IUnknown *>(given);
    }
    return {};
  }

  //  void IAxServerBase::EmitPropertyChanged(const char *property)
  void STDMETHODCALLTYPE EmitPropertyChanged(const char *property) override {
    if (taken[1]) {
      int handled = 0;
      CuteIAxServerBaseCall1 call = reinterpret_cast<CuteIAxServerBaseCall1>(taken[1]);
      call(this, property, &handled);
      if (handled) return;
    }
  }

  //  bool IAxServerBase::EmitRequestPropertyChange(const char *property)
  bool STDMETHODCALLTYPE EmitRequestPropertyChange(const char *property) override {
    if (taken[2]) {
      int handled = 0;
      CuteIAxServerBaseCall2 call = reinterpret_cast<CuteIAxServerBaseCall2>(taken[2]);
      bool given = call(this, property, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QObject *IAxServerBase::GetQObject() const
  QObject *STDMETHODCALLTYPE GetQObject() const override {
    if (taken[3]) {
      int handled = 0;
      CuteIAxServerBaseCall3 call = reinterpret_cast<CuteIAxServerBaseCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return {};
  }

  //  void IAxServerBase::ReportError(int code, const QString &src, const
  //      QString &desc, const QString &context)
  void STDMETHODCALLTYPE ReportError(int code, const QString &src, const QString &desc, const QString &context) override {
    if (taken[4]) {
      int handled = 0;
      CuteIAxServerBaseCall4 call = reinterpret_cast<CuteIAxServerBaseCall4>(taken[4]);
      call(this, code, &src, &desc, &context, &handled);
      if (handled) return;
    }
  }

  //  HRESULT IUnknown::QueryInterface(REFIID riid, void **ppvObject)
  HRESULT STDMETHODCALLTYPE QueryInterface(REFIID riid, void **ppvObject) override {
    if (taken[5]) {
      int handled = 0;
      CuteIAxServerBaseCall5 call = reinterpret_cast<CuteIAxServerBaseCall5>(taken[5]);
      HRESULT given = call(this, &riid, ppvObject, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  ULONG IUnknown::AddRef()
  ULONG STDMETHODCALLTYPE AddRef() override {
    if (taken[6]) {
      int handled = 0;
      CuteIAxServerBaseCall6 call = reinterpret_cast<CuteIAxServerBaseCall6>(taken[6]);
      ULONG given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  ULONG IUnknown::Release()
  ULONG STDMETHODCALLTYPE Release() override {
    if (taken[7]) {
      int handled = 0;
      CuteIAxServerBaseCall7 call = reinterpret_cast<CuteIAxServerBaseCall7>(taken[7]);
      ULONG given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  IUnknown *IAxServerBase::ClientSite() const
extern "C" Q_DECL_EXPORT
IUnknown *ritual_ZNK13IAxServerBase10ClientSiteEv(
    const IAxServerBase *self) {
  return self->ClientSite();
}

//  void IAxServerBase::EmitPropertyChanged(const char *property)
extern "C" Q_DECL_EXPORT
void ritual_ZN13IAxServerBase19EmitPropertyChangedEPKc(
    IAxServerBase *self,
    const char *property) {
  self->EmitPropertyChanged(property);
}

//  bool IAxServerBase::EmitRequestPropertyChange(const char *property)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13IAxServerBase25EmitRequestPropertyChangeEPKc(
    IAxServerBase *self,
    const char *property) {
  return self->EmitRequestPropertyChange(property);
}

//  QObject *IAxServerBase::GetQObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK13IAxServerBase10GetQObjectEv(const IAxServerBase *self) {
  return self->GetQObject();
}

//  void IAxServerBase::ReportError(int code, const QString &src, const
//      QString &desc, const QString &context)
extern "C" Q_DECL_EXPORT
void ritual_ZN13IAxServerBase11ReportErrorEiRK7QStringS2_S2_(
    IAxServerBase *self,
    int code,
    const QString *src,
    const QString *desc,
    const QString *context) {
  self->ReportError(code, *src, *desc, *context);
}

//  a Python function taken by a CuteIAxServerBase, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_IAxServerBase(
    IAxServerBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteIAxServerBase *>(self)->take(key, call);
}

#endif  // defined(Q_OS_WIN)
