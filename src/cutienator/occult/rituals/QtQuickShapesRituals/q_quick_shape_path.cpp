//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesglobal_p.h>
#include <QtQuickShapes/QtQuickShapes>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickShapePath that Python can take functions over in. Every QQuickShapePath
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_path)
typedef void (*CuteQQuickShapePathCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_path)
#if QT_CONFIG(quick_path)
typedef void (*CuteQQuickShapePathCall1)(const void *, int *);
#endif  // QT_CONFIG(quick_path)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickShapePathCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickShapePathCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapePathCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapePathCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapePathCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapePathCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapePathCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickShapePath : public QQuickShapePath {
public:
  using QQuickShapePath::QQuickShapePath;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_path)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_path)
#if QT_CONFIG(quick_path)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_path)
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

#if QT_CONFIG(quick_path)
  //  void QQuickPath::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickShapePathCall0 call = reinterpret_cast<CuteQQuickShapePathCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPath::componentComplete();
  }
#endif  // QT_CONFIG(quick_path)

#if QT_CONFIG(quick_path)
  //  void QQuickPath::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickShapePathCall1 call = reinterpret_cast<CuteQQuickShapePathCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPath::classBegin();
  }
#endif  // QT_CONFIG(quick_path)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickShapePathCall2 call = reinterpret_cast<CuteQQuickShapePathCall2>(taken[2]);
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
      CuteQQuickShapePathCall3 call = reinterpret_cast<CuteQQuickShapePathCall3>(taken[3]);
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
      CuteQQuickShapePathCall4 call = reinterpret_cast<CuteQQuickShapePathCall4>(taken[4]);
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
      CuteQQuickShapePathCall5 call = reinterpret_cast<CuteQQuickShapePathCall5>(taken[5]);
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
      CuteQQuickShapePathCall6 call = reinterpret_cast<CuteQQuickShapePathCall6>(taken[6]);
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
      CuteQQuickShapePathCall7 call = reinterpret_cast<CuteQQuickShapePathCall7>(taken[7]);
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
      CuteQQuickShapePathCall8 call = reinterpret_cast<CuteQQuickShapePathCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickShapePath::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickShapePath10metaObjectEv(
    const QQuickShapePath *self) {
  return self->metaObject();
}

//  QString QQuickShapePath::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickShapePath2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickShapePath::tr(s, c, n));
}

//  QQuickShapePath::QQuickShapePath(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickShapePath *ritual_ZN15QQuickShapePathC1EP7QObject(QObject *parent) {
  return new CuteQQuickShapePath(parent);
}

//  QQuickShapePath::~QQuickShapePath()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapePathD1Ev(QQuickShapePath *self) {
  delete self;
}

//  QColor QQuickShapePath::strokeColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QQuickShapePath11strokeColorEv(
    const QQuickShapePath *self) {
  return new QColor(self->strokeColor());
}

//  void QQuickShapePath::setStrokeColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapePath14setStrokeColorERK6QColor(
    QQuickShapePath *self,
    const QColor *color) {
  self->setStrokeColor(*color);
}

//  qreal QQuickShapePath::strokeWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickShapePath11strokeWidthEv(
    const QQuickShapePath *self) {
  return self->strokeWidth();
}

//  void QQuickShapePath::setStrokeWidth(qreal w)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapePath14setStrokeWidthEd(
    QQuickShapePath *self,
    qreal w) {
  self->setStrokeWidth(w);
}

//  void QQuickShapePath::setStrokeGradient(QQuickShapeGradient *gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapePath17setStrokeGradientEP19QQuickShapeGradient(
    QQuickShapePath *self,
    QQuickShapeGradient *gradient) {
  self->setStrokeGradient(gradient);
}

//  QQuickShapeGradient *QQuickShapePath::strokeGradient() const
extern "C" Q_DECL_EXPORT
QQuickShapeGradient *ritual_ZNK15QQuickShapePath14strokeGradientEv(
    const QQuickShapePath *self) {
  return self->strokeGradient();
}

//  void QQuickShapePath::resetStrokeGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapePath19resetStrokeGradientEv(
    QQuickShapePath *self) {
  self->resetStrokeGradient();
}

//  QColor QQuickShapePath::fillColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QQuickShapePath9fillColorEv(
    const QQuickShapePath *self) {
  return new QColor(self->fillColor());
}

//  void QQuickShapePath::setFillColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapePath12setFillColorERK6QColor(
    QQuickShapePath *self,
    const QColor *color) {
  self->setFillColor(*color);
}

//  FillRule QQuickShapePath::fillRule() const
extern "C" Q_DECL_EXPORT
QQuickShapePath::FillRule ritual_ZNK15QQuickShapePath8fillRuleEv(
    const QQuickShapePath *self) {
  return self->fillRule();
}

//  void QQuickShapePath::setFillRule(FillRule fillRule)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapePath11setFillRuleENS_8FillRuleE(
    QQuickShapePath *self,
    QQuickShapePath::FillRule fillRule) {
  self->setFillRule(fillRule);
}

//  JoinStyle QQuickShapePath::joinStyle() const
extern "C" Q_DECL_EXPORT
QQuickShapePath::JoinStyle ritual_ZNK15QQuickShapePath9joinStyleEv(
    const QQuickShapePath *self) {
  return self->joinStyle();
}

//  void QQuickShapePath::setJoinStyle(JoinStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapePath12setJoinStyleENS_9JoinStyleE(
    QQuickShapePath *self,
    QQuickShapePath::JoinStyle style) {
  self->setJoinStyle(style);
}

//  int QQuickShapePath::miterLimit() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickShapePath10miterLimitEv(const QQuickShapePath *self) {
  return self->miterLimit();
}

//  void QQuickShapePath::setMiterLimit(int limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapePath13setMiterLimitEi(
    QQuickShapePath *self,
    int limit) {
  self->setMiterLimit(limit);
}

//  CapStyle QQuickShapePath::capStyle() const
extern "C" Q_DECL_EXPORT
QQuickShapePath::CapStyle ritual_ZNK15QQuickShapePath8capStyleEv(
    const QQuickShapePath *self) {
  return self->capStyle();
}

//  void QQuickShapePath::setCapStyle(CapStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapePath11setCapStyleENS_8CapStyleE(
    QQuickShapePath *self,
    QQuickShapePath::CapStyle style) {
  self->setCapStyle(style);
}

//  StrokeStyle QQuickShapePath::strokeStyle() const
extern "C" Q_DECL_EXPORT
QQuickShapePath::StrokeStyle ritual_ZNK15QQuickShapePath11strokeStyleEv(
    const QQuickShapePath *self) {
  return self->strokeStyle();
}

//  void QQuickShapePath::setStrokeStyle(StrokeStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapePath14setStrokeStyleENS_11StrokeStyleE(
    QQuickShapePath *self,
    QQuickShapePath::StrokeStyle style) {
  self->setStrokeStyle(style);
}

//  qreal QQuickShapePath::dashOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickShapePath10dashOffsetEv(
    const QQuickShapePath *self) {
  return self->dashOffset();
}

//  void QQuickShapePath::setDashOffset(qreal offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapePath13setDashOffsetEd(
    QQuickShapePath *self,
    qreal offset) {
  self->setDashOffset(offset);
}

//  QQuickShapeGradient *QQuickShapePath::fillGradient() const
extern "C" Q_DECL_EXPORT
QQuickShapeGradient *ritual_ZNK15QQuickShapePath12fillGradientEv(
    const QQuickShapePath *self) {
  return self->fillGradient();
}

//  void QQuickShapePath::setFillGradient(QQuickShapeGradient *gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapePath15setFillGradientEP19QQuickShapeGradient(
    QQuickShapePath *self,
    QQuickShapeGradient *gradient) {
  self->setFillGradient(gradient);
}

//  void QQuickShapePath::resetFillGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapePath17resetFillGradientEv(QQuickShapePath *self) {
  self->resetFillGradient();
}

//  PathHints QQuickShapePath::pathHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickShapePath9pathHintsEv(const QQuickShapePath *self) {
  return static_cast<int>(self->pathHints().toInt());
}

//  void QQuickShapePath::setPathHints(PathHints newPathHints)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapePath12setPathHintsE6QFlagsINS_8PathHintEE(
    QQuickShapePath *self,
    int newPathHints) {
  self->setPathHints(
      QFlags<QQuickShapePath::PathHint>::fromInt(newPathHints));
}

//  QMatrix4x4 QQuickShapePath::fillTransform() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK15QQuickShapePath13fillTransformEv(
    const QQuickShapePath *self) {
  return new QMatrix4x4(self->fillTransform());
}

//  void QQuickShapePath::setFillTransform(const QMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapePath16setFillTransformERK10QMatrix4x4(
    QQuickShapePath *self,
    const QMatrix4x4 *matrix) {
  self->setFillTransform(*matrix);
}

//  QQuickItem *QQuickShapePath::fillItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK15QQuickShapePath8fillItemEv(
    const QQuickShapePath *self) {
  return self->fillItem();
}

//  void QQuickShapePath::setFillItem(QQuickItem *newFillItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapePath11setFillItemEP10QQuickItem(
    QQuickShapePath *self,
    QQuickItem *newFillItem) {
  self->setFillItem(newFillItem);
}

//  QQuickShapeTrim *QQuickShapePath::trim()
extern "C" Q_DECL_EXPORT
QQuickShapeTrim *ritual_ZN15QQuickShapePath4trimEv(QQuickShapePath *self) {
  return self->trim();
}

//  bool QQuickShapePath::hasTrim() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickShapePath7hasTrimEv(const QQuickShapePath *self) {
  return self->hasTrim();
}

//  bool QQuickShapePath::cosmeticStroke() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickShapePath14cosmeticStrokeEv(
    const QQuickShapePath *self) {
  return self->cosmeticStroke();
}

//  void QQuickShapePath::setCosmeticStroke(bool c)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapePath17setCosmeticStrokeEb(
    QQuickShapePath *self,
    bool c) {
  self->setCosmeticStroke(c);
}

//  QQuickShapePathPrivate *QQuickShapePath::d_func()
extern "C" Q_DECL_EXPORT
QQuickShapePathPrivate *ritual_ZN15QQuickShapePath6d_funcEv(
    QQuickShapePath *self) {
  return self->d_func();
}

//  const QQuickShapePathPrivate *QQuickShapePath::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickShapePathPrivate *ritual_ZNK15QQuickShapePath6d_funcEv(
    const QQuickShapePath *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickShapePath, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickShapePath(
    QQuickShapePath *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickShapePath *>(self)->take(key, call);
}
