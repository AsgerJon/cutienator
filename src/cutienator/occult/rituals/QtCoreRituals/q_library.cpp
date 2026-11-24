//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qlibrary.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(library)
#include <QtCore/qlibrary.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QLibrary that Python can take functions over in. Every QLibrary
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLibraryCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLibraryCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLibraryCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLibraryCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLibraryCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLibraryCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLibraryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLibrary : public QLibrary {
public:
  using QLibrary::QLibrary;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQLibraryCall0 call = reinterpret_cast<CuteQLibraryCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLibraryCall1 call = reinterpret_cast<CuteQLibraryCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLibraryCall2 call = reinterpret_cast<CuteQLibraryCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQLibraryCall3 call = reinterpret_cast<CuteQLibraryCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLibraryCall4 call = reinterpret_cast<CuteQLibraryCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLibraryCall5 call = reinterpret_cast<CuteQLibraryCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQLibraryCall6 call = reinterpret_cast<CuteQLibraryCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLibrary::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QLibrary10metaObjectEv(const QLibrary *self) {
  return self->metaObject();
}

//  QString QLibrary::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QLibrary2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QLibrary::tr(s, c, n));
}

//  QLibrary::QLibrary(QObject *parent)
extern "C" Q_DECL_EXPORT
QLibrary *ritual_ZN8QLibraryC1EP7QObject(QObject *parent) {
  return new CuteQLibrary(parent);
}

//  QLibrary::QLibrary(const QString &fileName, QObject *parent)
extern "C" Q_DECL_EXPORT
QLibrary *ritual_ZN8QLibraryC1ERK7QStringP7QObject(
    const QString *fileName,
    QObject *parent) {
  return new CuteQLibrary(*fileName, parent);
}

//  QLibrary::QLibrary(const QString &fileName, int verNum, QObject *parent)
extern "C" Q_DECL_EXPORT
QLibrary *ritual_ZN8QLibraryC1ERK7QStringiP7QObject(
    const QString *fileName,
    int verNum,
    QObject *parent) {
  return new CuteQLibrary(*fileName, verNum, parent);
}

//  QLibrary::QLibrary(const QString &fileName, const QString &version,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QLibrary *ritual_ZN8QLibraryC1ERK7QStringS2_P7QObject(
    const QString *fileName,
    const QString *version,
    QObject *parent) {
  return new CuteQLibrary(*fileName, *version, parent);
}

//  QLibrary::~QLibrary()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QLibraryD1Ev(QLibrary *self) {
  delete self;
}

//  bool QLibrary::load()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QLibrary4loadEv(QLibrary *self) {
  return self->load();
}

//  bool QLibrary::unload()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QLibrary6unloadEv(QLibrary *self) {
  return self->unload();
}

//  bool QLibrary::isLoaded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QLibrary8isLoadedEv(const QLibrary *self) {
  return self->isLoaded();
}

//  bool QLibrary::isLibrary(const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QLibrary9isLibraryERK7QString(const QString *fileName) {
  return QLibrary::isLibrary(*fileName);
}

//  void QLibrary::setFileName(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QLibrary11setFileNameERK7QString(
    QLibrary *self,
    const QString *fileName) {
  self->setFileName(*fileName);
}

//  QString QLibrary::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QLibrary8fileNameEv(const QLibrary *self) {
  return new QString(self->fileName());
}

//  void QLibrary::setFileNameAndVersion(const QString &fileName, int verNum)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QLibrary21setFileNameAndVersionERK7QStringi(
    QLibrary *self,
    const QString *fileName,
    int verNum) {
  self->setFileNameAndVersion(*fileName, verNum);
}

//  void QLibrary::setFileNameAndVersion(const QString &fileName, const
//      QString &version)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QLibrary21setFileNameAndVersionERK7QStringS2_(
    QLibrary *self,
    const QString *fileName,
    const QString *version) {
  self->setFileNameAndVersion(*fileName, *version);
}

//  QString QLibrary::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QLibrary11errorStringEv(const QLibrary *self) {
  return new QString(self->errorString());
}

//  void QLibrary::setLoadHints(LoadHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QLibrary12setLoadHintsE6QFlagsINS_8LoadHintEE(
    QLibrary *self,
    int hints) {
  self->setLoadHints(QFlags<QLibrary::LoadHint>::fromInt(hints));
}

//  LoadHints QLibrary::loadHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QLibrary9loadHintsEv(const QLibrary *self) {
  return static_cast<int>(self->loadHints().toInt());
}

//  a Python function taken by a CuteQLibrary, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLibrary(QLibrary *self, const char *key, void *call) {
  return static_cast<CuteQLibrary *>(self)->take(key, call);
}

#endif  // QT_CONFIG(library)
