//  Written by hand on 2026-11-25 from
//  QtAxServer/qaxbindable.h, Qt 6.12.0, from Qt's source. Kept as it
//  is when the generator runs again.
//  Qt builds ActiveQt for Windows only. AxServer is a static library,
//  all of it compiled into ours, so the class is taken as exported.
//  Nothing of it is left out.
#include <QtCore/qglobal.h>
#if defined(Q_OS_WIN)
#include <QtAxServer/qaxbindable.h>
#include <QtAxServer/qaxaggregated.h>
#include <QtCore/qiodevice.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QAxBindable that Python can take functions over in. Every
//  QAxBindable Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef void * (*CuteQAxBindableCall0)(const void *, int *);
typedef bool (*CuteQAxBindableCall1)(const void *, QIODevice *, const QString *, int *);
typedef bool (*CuteQAxBindableCall2)(const void *, QIODevice *, int *);
class CuteQAxBindable : public QAxBindable {
public:
  using QAxBindable::QAxBindable;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN11QAxBindable15createAggregateEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QAxBindable8readDataEP9QIODeviceRK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QAxBindable9writeDataEP9QIODevice")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QAxAggregated *QAxBindable::createAggregate()
  QAxAggregated *createAggregate() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAxBindableCall0 call = reinterpret_cast<CuteQAxBindableCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAxAggregated *>(given);
    }
    return QAxBindable::createAggregate();
  }

  //  bool QAxBindable::readData(QIODevice *source, const QString &format)
  bool readData(QIODevice *source, const QString &format) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAxBindableCall1 call = reinterpret_cast<CuteQAxBindableCall1>(taken[1]);
      bool given = call(this, source, &format, &handled);
      if (handled) return given;
    }
    return QAxBindable::readData(source, format);
  }

  //  bool QAxBindable::writeData(QIODevice *sink)
  bool writeData(QIODevice *sink) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAxBindableCall2 call = reinterpret_cast<CuteQAxBindableCall2>(taken[2]);
      bool given = call(this, sink, &handled);
      if (handled) return given;
    }
    return QAxBindable::writeData(sink);
  }
};

//  QAxBindable::QAxBindable()
extern "C" Q_DECL_EXPORT
QAxBindable *ritual_ZN11QAxBindableC1Ev() {
  return new CuteQAxBindable();
}

//  QAxBindable::~QAxBindable()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAxBindableD1Ev(QAxBindable *self) {
  delete self;
}

//  QAxAggregated *QAxBindable::createAggregate()
extern "C" Q_DECL_EXPORT
QAxAggregated *ritual_ZN11QAxBindable15createAggregateEv(QAxBindable *self) {
  return self->createAggregate();
}

//  void QAxBindable::reportError(int code, const QString &src, const QString
//      &desc, const QString &help)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAxBindable11reportErrorEiRK7QStringS2_S2_(
    QAxBindable *self,
    int code,
    const QString *src,
    const QString *desc,
    const QString *help) {
  self->reportError(code, *src, *desc, *help);
}

//  bool QAxBindable::readData(QIODevice *source, const QString &format)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QAxBindable8readDataEP9QIODeviceRK7QString(
    QAxBindable *self,
    QIODevice *source,
    const QString *format) {
  return self->readData(source, *format);
}

//  bool QAxBindable::writeData(QIODevice *sink)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QAxBindable9writeDataEP9QIODevice(
    QAxBindable *self,
    QIODevice *sink) {
  return self->writeData(sink);
}

//  bool QAxBindable::requestPropertyChange(const char *property)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QAxBindable21requestPropertyChangeEPKc(
    QAxBindable *self,
    const char *property) {
  return self->requestPropertyChange(property);
}

//  void QAxBindable::propertyChanged(const char *property)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAxBindable15propertyChangedEPKc(
    QAxBindable *self,
    const char *property) {
  self->propertyChanged(property);
}

//  IUnknown *QAxBindable::clientSite() const
extern "C" Q_DECL_EXPORT
IUnknown *ritual_ZNK11QAxBindable10clientSiteEv(const QAxBindable *self) {
  return self->clientSite();
}

//  a Python function taken by a CuteQAxBindable, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAxBindable(
    QAxBindable *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAxBindable *>(self)->take(key, call);
}

//  QAxAggregated *QAxBindable::createAggregate()
extern "C" Q_DECL_EXPORT
QAxAggregated *ritual_own_ZN11QAxBindable15createAggregateEv(
    QAxBindable *self) {
  return self->QAxBindable::createAggregate();
}

//  bool QAxBindable::readData(QIODevice *source, const QString &format)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QAxBindable8readDataEP9QIODeviceRK7QString(
    QAxBindable *self,
    QIODevice *source,
    const QString *format) {
  return self->QAxBindable::readData(source, *format);
}

//  bool QAxBindable::writeData(QIODevice *sink)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QAxBindable9writeDataEP9QIODevice(
    QAxBindable *self,
    QIODevice *sink) {
  return self->QAxBindable::writeData(sink);
}

#endif  // defined(Q_OS_WIN)
