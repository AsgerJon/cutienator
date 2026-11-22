//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtranslator.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qtranslator.h>
#include <QtCore/qstring.h>
#include <QtCore/qlocale.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QTranslator that Python can take functions over in. Every QTranslator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQTranslatorCall0)(const void *, int *);
typedef bool (*CuteQTranslatorCall1)(const void *, QEvent *, int *);
typedef bool (*CuteQTranslatorCall2)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQTranslatorCall3)(const void *, QTimerEvent *, int *);
typedef void (*CuteQTranslatorCall4)(const void *, QChildEvent *, int *);
typedef void (*CuteQTranslatorCall5)(const void *, QEvent *, int *);
typedef void (*CuteQTranslatorCall6)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQTranslatorCall7)(const void *, const QMetaMethod *, int *);
class CuteQTranslator : public QTranslator {
public:
  using QTranslator::QTranslator;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QTranslator7isEmptyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  bool QTranslator::isEmpty() const
  bool isEmpty() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTranslatorCall0 call = reinterpret_cast<CuteQTranslatorCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QTranslator::isEmpty();
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTranslatorCall1 call = reinterpret_cast<CuteQTranslatorCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTranslatorCall2 call = reinterpret_cast<CuteQTranslatorCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTranslatorCall3 call = reinterpret_cast<CuteQTranslatorCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTranslatorCall4 call = reinterpret_cast<CuteQTranslatorCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTranslatorCall5 call = reinterpret_cast<CuteQTranslatorCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTranslatorCall6 call = reinterpret_cast<CuteQTranslatorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQTranslatorCall7 call = reinterpret_cast<CuteQTranslatorCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QTranslator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QTranslator10metaObjectEv(
    const QTranslator *self) {
  return self->metaObject();
}

//  QString QTranslator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QTranslator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTranslator::tr(s, c, n));
}

//  QTranslator::QTranslator(QObject *parent)
extern "C" Q_DECL_EXPORT
QTranslator *ritual_ZN11QTranslatorC1EP7QObject(QObject *parent) {
  return new CuteQTranslator(parent);
}

//  QTranslator::~QTranslator()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTranslatorD1Ev(QTranslator *self) {
  delete self;
}

//  QString QTranslator::translate(const char *context, const char
//      *sourceText, const char *disambiguation, int n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTranslator9translateEPKcS1_S1_i(
    const QTranslator *self,
    const char *context,
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(
      self->translate(
          context,
          sourceText,
          disambiguation,
          n));
}

//  bool QTranslator::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTranslator7isEmptyEv(const QTranslator *self) {
  return self->isEmpty();
}

//  QString QTranslator::language() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTranslator8languageEv(const QTranslator *self) {
  return new QString(self->language());
}

//  QString QTranslator::filePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTranslator8filePathEv(const QTranslator *self) {
  return new QString(self->filePath());
}

//  bool QTranslator::load(const QString &filename, const QString &directory,
//      const QString &search_delimiters, const QString &suffix)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTranslator4loadERK7QStringS2_S2_S2_(
    QTranslator *self,
    const QString *filename,
    const QString *directory,
    const QString *search_delimiters,
    const QString *suffix) {
  return self->load(*filename, *directory, *search_delimiters, *suffix);
}

//  bool QTranslator::load(const QLocale &locale, const QString &filename,
//      const QString &prefix, const QString &directory, const QString
//      &suffix)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTranslator4loadERK7QLocaleRK7QStringS5_S5_S5_(
    QTranslator *self,
    const QLocale *locale,
    const QString *filename,
    const QString *prefix,
    const QString *directory,
    const QString *suffix) {
  return self->load(*locale, *filename, *prefix, *directory, *suffix);
}

//  a Python function taken by a CuteQTranslator, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTranslator(
    QTranslator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTranslator *>(self)->take(key, call);
}

//  bool QTranslator::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QTranslator7isEmptyEv(const QTranslator *self) {
  return self->QTranslator::isEmpty();
}
