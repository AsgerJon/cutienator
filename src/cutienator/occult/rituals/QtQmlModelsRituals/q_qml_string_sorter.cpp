//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlstringsorter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlstringsorter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlocale.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <QtCore/qcompare.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlStringSorter that Python can take functions over in. Every QQmlStringSorter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QPartialOrdering * (*CuteQQmlStringSorterCall0)(const void *, const QModelIndex *, const QModelIndex *, const QQmlSortFilterProxyModel *, int *);
typedef void (*CuteQQmlStringSorterCall1)(const void *, const QQmlSortFilterProxyModel *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlStringSorterCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlStringSorterCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlStringSorterCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlStringSorterCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlStringSorterCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlStringSorterCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlStringSorterCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlStringSorter : public QQmlStringSorter {
public:
  using QQmlStringSorter::QQmlStringSorter;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QQmlSorterBase7compareERK11QModelIndexS2_PK24QQmlSortFilterProxyModel")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQmlSorterBase6updateEPK24QQmlSortFilterProxyModel")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QPartialOrdering QQmlStringSorter::compare(const QModelIndex
  //      &sourceLeft, const QModelIndex &sourceRight, const
  //      QQmlSortFilterProxyModel *proxyModel) const
  QPartialOrdering compare(
      const QModelIndex &sourceLeft,
      const QModelIndex &sourceRight,
      const QQmlSortFilterProxyModel *proxyModel) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlStringSorterCall0 call = reinterpret_cast<CuteQQmlStringSorterCall0>(taken[0]);
      const QPartialOrdering * given = call(this, &sourceLeft, &sourceRight, proxyModel, &handled);
      if (handled && given) return *given;
    }
    return QQmlStringSorter::compare(sourceLeft, sourceRight, proxyModel);
  }

  //  void QQmlRoleSorter::update(const QQmlSortFilterProxyModel *a0)
  void update(const QQmlSortFilterProxyModel *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlStringSorterCall1 call = reinterpret_cast<CuteQQmlStringSorterCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlRoleSorter::update(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlStringSorterCall2 call = reinterpret_cast<CuteQQmlStringSorterCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlStringSorterCall3 call = reinterpret_cast<CuteQQmlStringSorterCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlStringSorterCall4 call = reinterpret_cast<CuteQQmlStringSorterCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlStringSorterCall5 call = reinterpret_cast<CuteQQmlStringSorterCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlStringSorterCall6 call = reinterpret_cast<CuteQQmlStringSorterCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlStringSorterCall7 call = reinterpret_cast<CuteQQmlStringSorterCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlStringSorterCall8 call = reinterpret_cast<CuteQQmlStringSorterCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlStringSorter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQmlStringSorter10metaObjectEv(
    const QQmlStringSorter *self) {
  return self->metaObject();
}

//  void *QQmlStringSorter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQmlStringSorter11qt_metacastEPKc(
    QQmlStringSorter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlStringSorter::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQmlStringSorter11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlStringSorter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlStringSorter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQmlStringSorter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlStringSorter::tr(s, c, n));
}

//  QQmlStringSorter::QQmlStringSorter(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlStringSorter *ritual_ZN16QQmlStringSorterC1EP7QObject(QObject *parent) {
  return new CuteQQmlStringSorter(parent);
}

//  QQmlStringSorter::~QQmlStringSorter()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlStringSorterD1Ev(QQmlStringSorter *self) {
  delete self;
}

//  Qt::CaseSensitivity QQmlStringSorter::caseSensitivity() const
extern "C" Q_DECL_EXPORT
Qt::CaseSensitivity ritual_ZNK16QQmlStringSorter15caseSensitivityEv(
    const QQmlStringSorter *self) {
  return self->caseSensitivity();
}

//  void QQmlStringSorter::setCaseSensitivity(Qt::CaseSensitivity
//      caseSensitivity)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlStringSorter18setCaseSensitivityEN2Qt15CaseSensitivityE(
    QQmlStringSorter *self,
    Qt::CaseSensitivity caseSensitivity) {
  self->setCaseSensitivity(caseSensitivity);
}

//  bool QQmlStringSorter::ignorePunctuation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlStringSorter17ignorePunctuationEv(
    const QQmlStringSorter *self) {
  return self->ignorePunctuation();
}

//  void QQmlStringSorter::setIgnorePunctuation(bool ignorePunctation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlStringSorter20setIgnorePunctuationEb(
    QQmlStringSorter *self,
    bool ignorePunctation) {
  self->setIgnorePunctuation(ignorePunctation);
}

//  QLocale QQmlStringSorter::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK16QQmlStringSorter6localeEv(
    const QQmlStringSorter *self) {
  return new QLocale(self->locale());
}

//  void QQmlStringSorter::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlStringSorter9setLocaleERK7QLocale(
    QQmlStringSorter *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  bool QQmlStringSorter::numericMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlStringSorter11numericModeEv(
    const QQmlStringSorter *self) {
  return self->numericMode();
}

//  void QQmlStringSorter::setNumericMode(bool numericMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlStringSorter14setNumericModeEb(
    QQmlStringSorter *self,
    bool numericMode) {
  self->setNumericMode(numericMode);
}

//  QPartialOrdering QQmlStringSorter::compare(const QModelIndex &sourceLeft,
//      const QModelIndex &sourceRight, const QQmlSortFilterProxyModel
//      *proxyModel) const
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_ZNK16QQmlStringSorter7compareERK11QModelIndexS2_PK24QQmlSortFilterProxyModel(
    const QQmlStringSorter *self,
    const QModelIndex *sourceLeft,
    const QModelIndex *sourceRight,
    const QQmlSortFilterProxyModel *proxyModel) {
  return new QPartialOrdering(
      self->compare(
          *sourceLeft,
          *sourceRight,
          proxyModel));
}

//  void QQmlStringSorter::caseSensitivityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlStringSorter22caseSensitivityChangedEv(
    QQmlStringSorter *self) {
  self->caseSensitivityChanged();
}

//  void QQmlStringSorter::ignorePunctuationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlStringSorter24ignorePunctuationChangedEv(
    QQmlStringSorter *self) {
  self->ignorePunctuationChanged();
}

//  void QQmlStringSorter::localeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlStringSorter13localeChangedEv(QQmlStringSorter *self) {
  self->localeChanged();
}

//  void QQmlStringSorter::numericModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlStringSorter18numericModeChangedEv(
    QQmlStringSorter *self) {
  self->numericModeChanged();
}

//  QQmlStringSorterPrivate *QQmlStringSorter::d_func()
extern "C" Q_DECL_EXPORT
QQmlStringSorterPrivate *ritual_ZN16QQmlStringSorter6d_funcEv(
    QQmlStringSorter *self) {
  return self->d_func();
}

//  const QQmlStringSorterPrivate *QQmlStringSorter::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlStringSorterPrivate *ritual_ZNK16QQmlStringSorter6d_funcEv(
    const QQmlStringSorter *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQmlStringSorter, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlStringSorter(
    QQmlStringSorter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlStringSorter *>(self)->take(key, call);
}

//  QPartialOrdering QQmlStringSorter::compare(const QModelIndex &sourceLeft,
//      const QModelIndex &sourceRight, const QQmlSortFilterProxyModel
//      *proxyModel) const
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_own_ZNK16QQmlStringSorter7compareERK11QModelIndexS2_PK24QQmlSortFilterProxyModel(
    const QQmlStringSorter *self,
    const QModelIndex *sourceLeft,
    const QModelIndex *sourceRight,
    const QQmlSortFilterProxyModel *proxyModel) {
  return new QPartialOrdering(
      self->QQmlStringSorter::compare(
          *sourceLeft,
          *sourceRight,
          proxyModel));
}

#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
