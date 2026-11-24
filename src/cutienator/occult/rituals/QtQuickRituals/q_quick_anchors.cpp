//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanchors_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanchors_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanchors_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickAnchors that Python can take functions over in. Every QQuickAnchors
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAnchorsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAnchorsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnchorsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnchorsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnchorsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnchorsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnchorsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickAnchors : public QQuickAnchors {
public:
  using QQuickAnchors::QQuickAnchors;
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
      CuteQQuickAnchorsCall0 call = reinterpret_cast<CuteQQuickAnchorsCall0>(taken[0]);
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
      CuteQQuickAnchorsCall1 call = reinterpret_cast<CuteQQuickAnchorsCall1>(taken[1]);
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
      CuteQQuickAnchorsCall2 call = reinterpret_cast<CuteQQuickAnchorsCall2>(taken[2]);
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
      CuteQQuickAnchorsCall3 call = reinterpret_cast<CuteQQuickAnchorsCall3>(taken[3]);
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
      CuteQQuickAnchorsCall4 call = reinterpret_cast<CuteQQuickAnchorsCall4>(taken[4]);
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
      CuteQQuickAnchorsCall5 call = reinterpret_cast<CuteQQuickAnchorsCall5>(taken[5]);
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
      CuteQQuickAnchorsCall6 call = reinterpret_cast<CuteQQuickAnchorsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickAnchors::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQuickAnchors10metaObjectEv(
    const QQuickAnchors *self) {
  return self->metaObject();
}

//  QString QQuickAnchors::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQuickAnchors2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAnchors::tr(s, c, n));
}

//  void QQuickAnchors::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors22qt_qmlMarker_anonymousEv(
    QQuickAnchors *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickAnchors::QQuickAnchors(QQuickItem *item, QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickAnchors *ritual_ZN13QQuickAnchorsC1EP10QQuickItemP7QObject(
    QQuickItem *item,
    QObject *parent) {
  return new CuteQQuickAnchors(item, parent);
}

//  QQuickAnchors::~QQuickAnchors()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchorsD1Ev(QQuickAnchors *self) {
  delete self;
}

//  QQuickAnchorLine QQuickAnchors::left() const
extern "C" Q_DECL_EXPORT
QQuickAnchorLine *ritual_ZNK13QQuickAnchors4leftEv(
    const QQuickAnchors *self) {
  return new QQuickAnchorLine(self->left());
}

//  void QQuickAnchors::setLeft(const QQuickAnchorLine &edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors7setLeftERK16QQuickAnchorLine(
    QQuickAnchors *self,
    const QQuickAnchorLine *edge) {
  self->setLeft(*edge);
}

//  void QQuickAnchors::resetLeft()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors9resetLeftEv(QQuickAnchors *self) {
  self->resetLeft();
}

//  QQuickAnchorLine QQuickAnchors::right() const
extern "C" Q_DECL_EXPORT
QQuickAnchorLine *ritual_ZNK13QQuickAnchors5rightEv(
    const QQuickAnchors *self) {
  return new QQuickAnchorLine(self->right());
}

//  void QQuickAnchors::setRight(const QQuickAnchorLine &edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors8setRightERK16QQuickAnchorLine(
    QQuickAnchors *self,
    const QQuickAnchorLine *edge) {
  self->setRight(*edge);
}

//  void QQuickAnchors::resetRight()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors10resetRightEv(QQuickAnchors *self) {
  self->resetRight();
}

//  QQuickAnchorLine QQuickAnchors::horizontalCenter() const
extern "C" Q_DECL_EXPORT
QQuickAnchorLine *ritual_ZNK13QQuickAnchors16horizontalCenterEv(
    const QQuickAnchors *self) {
  return new QQuickAnchorLine(self->horizontalCenter());
}

//  void QQuickAnchors::setHorizontalCenter(const QQuickAnchorLine &edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors19setHorizontalCenterERK16QQuickAnchorLine(
    QQuickAnchors *self,
    const QQuickAnchorLine *edge) {
  self->setHorizontalCenter(*edge);
}

//  void QQuickAnchors::resetHorizontalCenter()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors21resetHorizontalCenterEv(QQuickAnchors *self) {
  self->resetHorizontalCenter();
}

//  QQuickAnchorLine QQuickAnchors::top() const
extern "C" Q_DECL_EXPORT
QQuickAnchorLine *ritual_ZNK13QQuickAnchors3topEv(
    const QQuickAnchors *self) {
  return new QQuickAnchorLine(self->top());
}

//  void QQuickAnchors::setTop(const QQuickAnchorLine &edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors6setTopERK16QQuickAnchorLine(
    QQuickAnchors *self,
    const QQuickAnchorLine *edge) {
  self->setTop(*edge);
}

//  void QQuickAnchors::resetTop()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors8resetTopEv(QQuickAnchors *self) {
  self->resetTop();
}

//  QQuickAnchorLine QQuickAnchors::bottom() const
extern "C" Q_DECL_EXPORT
QQuickAnchorLine *ritual_ZNK13QQuickAnchors6bottomEv(
    const QQuickAnchors *self) {
  return new QQuickAnchorLine(self->bottom());
}

//  void QQuickAnchors::setBottom(const QQuickAnchorLine &edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors9setBottomERK16QQuickAnchorLine(
    QQuickAnchors *self,
    const QQuickAnchorLine *edge) {
  self->setBottom(*edge);
}

//  void QQuickAnchors::resetBottom()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors11resetBottomEv(QQuickAnchors *self) {
  self->resetBottom();
}

//  QQuickAnchorLine QQuickAnchors::verticalCenter() const
extern "C" Q_DECL_EXPORT
QQuickAnchorLine *ritual_ZNK13QQuickAnchors14verticalCenterEv(
    const QQuickAnchors *self) {
  return new QQuickAnchorLine(self->verticalCenter());
}

//  void QQuickAnchors::setVerticalCenter(const QQuickAnchorLine &edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors17setVerticalCenterERK16QQuickAnchorLine(
    QQuickAnchors *self,
    const QQuickAnchorLine *edge) {
  self->setVerticalCenter(*edge);
}

//  void QQuickAnchors::resetVerticalCenter()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors19resetVerticalCenterEv(QQuickAnchors *self) {
  self->resetVerticalCenter();
}

//  QQuickAnchorLine QQuickAnchors::baseline() const
extern "C" Q_DECL_EXPORT
QQuickAnchorLine *ritual_ZNK13QQuickAnchors8baselineEv(
    const QQuickAnchors *self) {
  return new QQuickAnchorLine(self->baseline());
}

//  void QQuickAnchors::setBaseline(const QQuickAnchorLine &edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors11setBaselineERK16QQuickAnchorLine(
    QQuickAnchors *self,
    const QQuickAnchorLine *edge) {
  self->setBaseline(*edge);
}

//  void QQuickAnchors::resetBaseline()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors13resetBaselineEv(QQuickAnchors *self) {
  self->resetBaseline();
}

//  qreal QQuickAnchors::leftMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickAnchors10leftMarginEv(const QQuickAnchors *self) {
  return self->leftMargin();
}

//  void QQuickAnchors::setLeftMargin(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors13setLeftMarginEd(
    QQuickAnchors *self,
    qreal a0) {
  self->setLeftMargin(a0);
}

//  void QQuickAnchors::resetLeftMargin()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors15resetLeftMarginEv(QQuickAnchors *self) {
  self->resetLeftMargin();
}

//  qreal QQuickAnchors::rightMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickAnchors11rightMarginEv(const QQuickAnchors *self) {
  return self->rightMargin();
}

//  void QQuickAnchors::setRightMargin(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors14setRightMarginEd(
    QQuickAnchors *self,
    qreal a0) {
  self->setRightMargin(a0);
}

//  void QQuickAnchors::resetRightMargin()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors16resetRightMarginEv(QQuickAnchors *self) {
  self->resetRightMargin();
}

//  qreal QQuickAnchors::horizontalCenterOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickAnchors22horizontalCenterOffsetEv(
    const QQuickAnchors *self) {
  return self->horizontalCenterOffset();
}

//  void QQuickAnchors::setHorizontalCenterOffset(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors25setHorizontalCenterOffsetEd(
    QQuickAnchors *self,
    qreal a0) {
  self->setHorizontalCenterOffset(a0);
}

//  qreal QQuickAnchors::topMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickAnchors9topMarginEv(const QQuickAnchors *self) {
  return self->topMargin();
}

//  void QQuickAnchors::setTopMargin(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors12setTopMarginEd(
    QQuickAnchors *self,
    qreal a0) {
  self->setTopMargin(a0);
}

//  void QQuickAnchors::resetTopMargin()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors14resetTopMarginEv(QQuickAnchors *self) {
  self->resetTopMargin();
}

//  qreal QQuickAnchors::bottomMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickAnchors12bottomMarginEv(const QQuickAnchors *self) {
  return self->bottomMargin();
}

//  void QQuickAnchors::setBottomMargin(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors15setBottomMarginEd(
    QQuickAnchors *self,
    qreal a0) {
  self->setBottomMargin(a0);
}

//  void QQuickAnchors::resetBottomMargin()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors17resetBottomMarginEv(QQuickAnchors *self) {
  self->resetBottomMargin();
}

//  qreal QQuickAnchors::margins() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickAnchors7marginsEv(const QQuickAnchors *self) {
  return self->margins();
}

//  void QQuickAnchors::setMargins(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors10setMarginsEd(QQuickAnchors *self, qreal a0) {
  self->setMargins(a0);
}

//  qreal QQuickAnchors::verticalCenterOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickAnchors20verticalCenterOffsetEv(
    const QQuickAnchors *self) {
  return self->verticalCenterOffset();
}

//  void QQuickAnchors::setVerticalCenterOffset(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors23setVerticalCenterOffsetEd(
    QQuickAnchors *self,
    qreal a0) {
  self->setVerticalCenterOffset(a0);
}

//  qreal QQuickAnchors::baselineOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickAnchors14baselineOffsetEv(
    const QQuickAnchors *self) {
  return self->baselineOffset();
}

//  void QQuickAnchors::setBaselineOffset(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors17setBaselineOffsetEd(
    QQuickAnchors *self,
    qreal a0) {
  self->setBaselineOffset(a0);
}

//  QQuickItem *QQuickAnchors::fill() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK13QQuickAnchors4fillEv(const QQuickAnchors *self) {
  return self->fill();
}

//  void QQuickAnchors::setFill(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors7setFillEP10QQuickItem(
    QQuickAnchors *self,
    QQuickItem *a0) {
  self->setFill(a0);
}

//  void QQuickAnchors::resetFill()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors9resetFillEv(QQuickAnchors *self) {
  self->resetFill();
}

//  QQuickItem *QQuickAnchors::centerIn() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK13QQuickAnchors8centerInEv(const QQuickAnchors *self) {
  return self->centerIn();
}

//  void QQuickAnchors::setCenterIn(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors11setCenterInEP10QQuickItem(
    QQuickAnchors *self,
    QQuickItem *a0) {
  self->setCenterIn(a0);
}

//  void QQuickAnchors::resetCenterIn()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors13resetCenterInEv(QQuickAnchors *self) {
  self->resetCenterIn();
}

//  Anchors QQuickAnchors::usedAnchors() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QQuickAnchors11usedAnchorsEv(const QQuickAnchors *self) {
  return static_cast<int>(self->usedAnchors().toInt());
}

//  Qt::Orientations QQuickAnchors::activeDirections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QQuickAnchors16activeDirectionsEv(
    const QQuickAnchors *self) {
  return static_cast<int>(self->activeDirections().toInt());
}

//  bool QQuickAnchors::mirrored()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QQuickAnchors8mirroredEv(QQuickAnchors *self) {
  return self->mirrored();
}

//  bool QQuickAnchors::alignWhenCentered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickAnchors17alignWhenCenteredEv(
    const QQuickAnchors *self) {
  return self->alignWhenCentered();
}

//  void QQuickAnchors::setAlignWhenCentered(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors20setAlignWhenCenteredEb(
    QQuickAnchors *self,
    bool a0) {
  self->setAlignWhenCentered(a0);
}

//  void QQuickAnchors::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors10classBeginEv(QQuickAnchors *self) {
  self->classBegin();
}

//  void QQuickAnchors::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickAnchors17componentCompleteEv(QQuickAnchors *self) {
  self->componentComplete();
}

//  QQuickAnchorsPrivate *QQuickAnchors::d_func()
extern "C" Q_DECL_EXPORT
QQuickAnchorsPrivate *ritual_ZN13QQuickAnchors6d_funcEv(
    QQuickAnchors *self) {
  return self->d_func();
}

//  const QQuickAnchorsPrivate *QQuickAnchors::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickAnchorsPrivate *ritual_ZNK13QQuickAnchors6d_funcEv(
    const QQuickAnchors *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickAnchors, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAnchors(
    QQuickAnchors *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAnchors *>(self)->take(key, call);
}
