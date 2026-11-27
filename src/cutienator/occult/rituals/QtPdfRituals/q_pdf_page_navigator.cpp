//  Written by dev_tooling.RitualGenerator from the records of
//  QtPdf/qpdfpagenavigator.h, Qt 6.12.0. Changes made here are lost.
#include <QtPdf/qpdfpagenavigator.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtPdf/qpdflink.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPdfPageNavigator that Python can take functions over in. Every QPdfPageNavigator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPdfPageNavigatorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPdfPageNavigatorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfPageNavigatorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfPageNavigatorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfPageNavigatorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfPageNavigatorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfPageNavigatorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPdfPageNavigator : public QPdfPageNavigator {
public:
  using QPdfPageNavigator::QPdfPageNavigator;
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
      CuteQPdfPageNavigatorCall0 call = reinterpret_cast<CuteQPdfPageNavigatorCall0>(taken[0]);
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
      CuteQPdfPageNavigatorCall1 call = reinterpret_cast<CuteQPdfPageNavigatorCall1>(taken[1]);
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
      CuteQPdfPageNavigatorCall2 call = reinterpret_cast<CuteQPdfPageNavigatorCall2>(taken[2]);
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
      CuteQPdfPageNavigatorCall3 call = reinterpret_cast<CuteQPdfPageNavigatorCall3>(taken[3]);
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
      CuteQPdfPageNavigatorCall4 call = reinterpret_cast<CuteQPdfPageNavigatorCall4>(taken[4]);
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
      CuteQPdfPageNavigatorCall5 call = reinterpret_cast<CuteQPdfPageNavigatorCall5>(taken[5]);
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
      CuteQPdfPageNavigatorCall6 call = reinterpret_cast<CuteQPdfPageNavigatorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPdfPageNavigator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QPdfPageNavigator10metaObjectEv(
    const QPdfPageNavigator *self) {
  return self->metaObject();
}

//  void *QPdfPageNavigator::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QPdfPageNavigator11qt_metacastEPKc(
    QPdfPageNavigator *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPdfPageNavigator::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QPdfPageNavigator11qt_metacallEN11QMetaObject4CallEiPPv(
    QPdfPageNavigator *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPdfPageNavigator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QPdfPageNavigator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPdfPageNavigator::tr(s, c, n));
}

//  QPdfPageNavigator::QPdfPageNavigator()
extern "C" Q_DECL_EXPORT
QPdfPageNavigator *ritual_ZN17QPdfPageNavigatorC1Ev() {
  return new CuteQPdfPageNavigator();
}

//  QPdfPageNavigator::QPdfPageNavigator(QObject *parent)
extern "C" Q_DECL_EXPORT
QPdfPageNavigator *ritual_ZN17QPdfPageNavigatorC1EP7QObject(
    QObject *parent) {
  return new CuteQPdfPageNavigator(parent);
}

//  QPdfPageNavigator::~QPdfPageNavigator()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfPageNavigatorD1Ev(QPdfPageNavigator *self) {
  delete self;
}

//  int QPdfPageNavigator::currentPage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QPdfPageNavigator11currentPageEv(
    const QPdfPageNavigator *self) {
  return self->currentPage();
}

//  QPointF QPdfPageNavigator::currentLocation() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK17QPdfPageNavigator15currentLocationEv(
    const QPdfPageNavigator *self) {
  return new QPointF(self->currentLocation());
}

//  qreal QPdfPageNavigator::currentZoom() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QPdfPageNavigator11currentZoomEv(
    const QPdfPageNavigator *self) {
  return self->currentZoom();
}

//  bool QPdfPageNavigator::backAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QPdfPageNavigator13backAvailableEv(
    const QPdfPageNavigator *self) {
  return self->backAvailable();
}

//  bool QPdfPageNavigator::forwardAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QPdfPageNavigator16forwardAvailableEv(
    const QPdfPageNavigator *self) {
  return self->forwardAvailable();
}

//  void QPdfPageNavigator::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfPageNavigator5clearEv(QPdfPageNavigator *self) {
  self->clear();
}

//  void QPdfPageNavigator::jump(QPdfLink destination)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfPageNavigator4jumpE8QPdfLink(
    QPdfPageNavigator *self,
    const QPdfLink *destination) {
  self->jump(*destination);
}

//  void QPdfPageNavigator::jump(int page, const QPointF &location, qreal
//      zoom)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfPageNavigator4jumpEiRK7QPointFd(
    QPdfPageNavigator *self,
    int page,
    const QPointF *location,
    qreal zoom) {
  self->jump(page, *location, zoom);
}

//  void QPdfPageNavigator::update(int page, const QPointF &location, qreal
//      zoom)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfPageNavigator6updateEiRK7QPointFd(
    QPdfPageNavigator *self,
    int page,
    const QPointF *location,
    qreal zoom) {
  self->update(page, *location, zoom);
}

//  void QPdfPageNavigator::forward()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfPageNavigator7forwardEv(QPdfPageNavigator *self) {
  self->forward();
}

//  void QPdfPageNavigator::back()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfPageNavigator4backEv(QPdfPageNavigator *self) {
  self->back();
}

//  void QPdfPageNavigator::currentPageChanged(int page)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfPageNavigator18currentPageChangedEi(
    QPdfPageNavigator *self,
    int page) {
  self->currentPageChanged(page);
}

//  void QPdfPageNavigator::currentLocationChanged(QPointF location)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfPageNavigator22currentLocationChangedE7QPointF(
    QPdfPageNavigator *self,
    const QPointF *location) {
  self->currentLocationChanged(*location);
}

//  void QPdfPageNavigator::currentZoomChanged(qreal zoom)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfPageNavigator18currentZoomChangedEd(
    QPdfPageNavigator *self,
    qreal zoom) {
  self->currentZoomChanged(zoom);
}

//  void QPdfPageNavigator::backAvailableChanged(bool available)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfPageNavigator20backAvailableChangedEb(
    QPdfPageNavigator *self,
    bool available) {
  self->backAvailableChanged(available);
}

//  void QPdfPageNavigator::forwardAvailableChanged(bool available)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfPageNavigator23forwardAvailableChangedEb(
    QPdfPageNavigator *self,
    bool available) {
  self->forwardAvailableChanged(available);
}

//  void QPdfPageNavigator::jumped(QPdfLink current)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPdfPageNavigator6jumpedE8QPdfLink(
    QPdfPageNavigator *self,
    const QPdfLink *current) {
  self->jumped(*current);
}

//  QPdfLink QPdfPageNavigator::currentLink() const
extern "C" Q_DECL_EXPORT
QPdfLink *ritual_ZNK17QPdfPageNavigator11currentLinkEv(
    const QPdfPageNavigator *self) {
  return new QPdfLink(self->currentLink());
}

//  a Python function taken by a CuteQPdfPageNavigator, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPdfPageNavigator(
    QPdfPageNavigator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPdfPageNavigator *>(self)->take(key, call);
}
