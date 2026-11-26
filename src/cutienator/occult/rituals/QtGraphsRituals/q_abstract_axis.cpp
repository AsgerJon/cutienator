//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qabstractaxis.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom)))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qabstractaxis.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtGui/qfont.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAbstractAxis that Python can take functions over in. Every QAbstractAxis
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQAbstractAxisCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractAxisCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractAxisCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAxisCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAxisCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAxisCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAxisCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAxisCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractAxis : public QAbstractAxis {
public:
  using QAbstractAxis::QAbstractAxis;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13QAbstractAxis4typeEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  AxisType QAbstractAxis::type() const
  QAbstractAxis::AxisType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractAxisCall0 call = reinterpret_cast<CuteQAbstractAxisCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractAxis::AxisType>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractAxisCall1 call = reinterpret_cast<CuteQAbstractAxisCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractAxisCall2 call = reinterpret_cast<CuteQAbstractAxisCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractAxisCall3 call = reinterpret_cast<CuteQAbstractAxisCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractAxisCall4 call = reinterpret_cast<CuteQAbstractAxisCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractAxisCall5 call = reinterpret_cast<CuteQAbstractAxisCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractAxisCall6 call = reinterpret_cast<CuteQAbstractAxisCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractAxisCall7 call = reinterpret_cast<CuteQAbstractAxisCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractAxis::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QAbstractAxis10metaObjectEv(
    const QAbstractAxis *self) {
  return self->metaObject();
}

//  void *QAbstractAxis::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QAbstractAxis11qt_metacastEPKc(
    QAbstractAxis *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractAxis::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QAbstractAxis11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractAxis *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractAxis::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QAbstractAxis2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractAxis::tr(s, c, n));
}

//  void QAbstractAxis::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis20qt_qmlMarker_foreignEv(QAbstractAxis *self) {
  self->qt_qmlMarker_foreign();
}

//  void QAbstractAxis::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis24qt_qmlMarker_uncreatableEv(
    QAbstractAxis *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QAbstractAxisPrivate *QAbstractAxis::d_func()
extern "C" Q_DECL_EXPORT
QAbstractAxisPrivate *ritual_ZN13QAbstractAxis6d_funcEv(
    QAbstractAxis *self) {
  return self->d_func();
}

//  const QAbstractAxisPrivate *QAbstractAxis::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractAxisPrivate *ritual_ZNK13QAbstractAxis6d_funcEv(
    const QAbstractAxis *self) {
  return self->d_func();
}

//  QAbstractAxis::QAbstractAxis(QAbstractAxisPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN13QAbstractAxisC1ER20QAbstractAxisPrivateP7QObject(
    QAbstractAxisPrivate *dd,
    QObject *parent) {
  return new CuteQAbstractAxis(*dd, parent);
}

//  QAbstractAxis::~QAbstractAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxisD1Ev(QAbstractAxis *self) {
  delete self;
}

//  AxisType QAbstractAxis::type() const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_ZNK13QAbstractAxis4typeEv(
    const QAbstractAxis *self) {
  return self->type();
}

//  bool QAbstractAxis::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QAbstractAxis9isVisibleEv(const QAbstractAxis *self) {
  return self->isVisible();
}

//  void QAbstractAxis::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis10setVisibleEb(
    QAbstractAxis *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QAbstractAxis::show()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis4showEv(QAbstractAxis *self) {
  self->show();
}

//  void QAbstractAxis::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis4hideEv(QAbstractAxis *self) {
  self->hide();
}

//  bool QAbstractAxis::isLineVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QAbstractAxis13isLineVisibleEv(const QAbstractAxis *self) {
  return self->isLineVisible();
}

//  void QAbstractAxis::setLineVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis14setLineVisibleEb(
    QAbstractAxis *self,
    bool visible) {
  self->setLineVisible(visible);
}

//  bool QAbstractAxis::isGridVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QAbstractAxis13isGridVisibleEv(const QAbstractAxis *self) {
  return self->isGridVisible();
}

//  void QAbstractAxis::setGridVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis14setGridVisibleEb(
    QAbstractAxis *self,
    bool visible) {
  self->setGridVisible(visible);
}

//  bool QAbstractAxis::isSubGridVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QAbstractAxis16isSubGridVisibleEv(
    const QAbstractAxis *self) {
  return self->isSubGridVisible();
}

//  void QAbstractAxis::setSubGridVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis17setSubGridVisibleEb(
    QAbstractAxis *self,
    bool visible) {
  self->setSubGridVisible(visible);
}

//  bool QAbstractAxis::labelsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QAbstractAxis13labelsVisibleEv(const QAbstractAxis *self) {
  return self->labelsVisible();
}

//  void QAbstractAxis::setLabelsVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis16setLabelsVisibleEb(
    QAbstractAxis *self,
    bool visible) {
  self->setLabelsVisible(visible);
}

//  void QAbstractAxis::setLabelsAngle(qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis14setLabelsAngleEd(
    QAbstractAxis *self,
    qreal angle) {
  self->setLabelsAngle(angle);
}

//  qreal QAbstractAxis::labelsAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QAbstractAxis11labelsAngleEv(const QAbstractAxis *self) {
  return self->labelsAngle();
}

//  QQmlComponent *QAbstractAxis::labelDelegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK13QAbstractAxis13labelDelegateEv(
    const QAbstractAxis *self) {
  return self->labelDelegate();
}

//  void QAbstractAxis::setLabelDelegate(QQmlComponent *newLabelDelegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis16setLabelDelegateEP13QQmlComponent(
    QAbstractAxis *self,
    QQmlComponent *newLabelDelegate) {
  self->setLabelDelegate(newLabelDelegate);
}

//  bool QAbstractAxis::isTitleVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QAbstractAxis14isTitleVisibleEv(const QAbstractAxis *self) {
  return self->isTitleVisible();
}

//  void QAbstractAxis::setTitleVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis15setTitleVisibleEb(
    QAbstractAxis *self,
    bool visible) {
  self->setTitleVisible(visible);
}

//  void QAbstractAxis::setTitleColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis13setTitleColorE6QColor(
    QAbstractAxis *self,
    const QColor *color) {
  self->setTitleColor(*color);
}

//  QColor QAbstractAxis::titleColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK13QAbstractAxis10titleColorEv(const QAbstractAxis *self) {
  return new QColor(self->titleColor());
}

//  void QAbstractAxis::setTitleFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis12setTitleFontERK5QFont(
    QAbstractAxis *self,
    const QFont *font) {
  self->setTitleFont(*font);
}

//  QFont QAbstractAxis::titleFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK13QAbstractAxis9titleFontEv(const QAbstractAxis *self) {
  return new QFont(self->titleFont());
}

//  void QAbstractAxis::setTitleText(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis12setTitleTextERK7QString(
    QAbstractAxis *self,
    const QString *title) {
  self->setTitleText(*title);
}

//  QString QAbstractAxis::titleText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QAbstractAxis9titleTextEv(const QAbstractAxis *self) {
  return new QString(self->titleText());
}

//  Qt::Alignment QAbstractAxis::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QAbstractAxis9alignmentEv(const QAbstractAxis *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QAbstractAxis::setAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QAbstractAxis *self,
    int alignment) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  Qt::TextElideMode QAbstractAxis::textElideMode() const
extern "C" Q_DECL_EXPORT
Qt::TextElideMode ritual_ZNK13QAbstractAxis13textElideModeEv(
    const QAbstractAxis *self) {
  return self->textElideMode();
}

//  void QAbstractAxis::setTextElideMode(Qt::TextElideMode elideMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis16setTextElideModeEN2Qt13TextElideModeE(
    QAbstractAxis *self,
    Qt::TextElideMode elideMode) {
  self->setTextElideMode(elideMode);
}

//  void QAbstractAxis::setSubColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis11setSubColorE6QColor(
    QAbstractAxis *self,
    const QColor *color) {
  self->setSubColor(*color);
}

//  QColor QAbstractAxis::subColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK13QAbstractAxis8subColorEv(const QAbstractAxis *self) {
  return new QColor(self->subColor());
}

//  void QAbstractAxis::setColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis8setColorE6QColor(
    QAbstractAxis *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QColor QAbstractAxis::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK13QAbstractAxis5colorEv(const QAbstractAxis *self) {
  return new QColor(self->color());
}

//  void QAbstractAxis::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis6setMinERK8QVariant(
    QAbstractAxis *self,
    const QVariant *min) {
  self->setMin(*min);
}

//  void QAbstractAxis::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis6setMaxERK8QVariant(
    QAbstractAxis *self,
    const QVariant *max) {
  self->setMax(*max);
}

//  void QAbstractAxis::setRange(const QVariant &min, const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis8setRangeERK8QVariantS2_(
    QAbstractAxis *self,
    const QVariant *min,
    const QVariant *max) {
  self->setRange(*min, *max);
}

//  void QAbstractAxis::visibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis14visibleChangedEb(
    QAbstractAxis *self,
    bool visible) {
  self->visibleChanged(visible);
}

//  void QAbstractAxis::lineVisibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis18lineVisibleChangedEb(
    QAbstractAxis *self,
    bool visible) {
  self->lineVisibleChanged(visible);
}

//  void QAbstractAxis::labelsVisibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis20labelsVisibleChangedEb(
    QAbstractAxis *self,
    bool visible) {
  self->labelsVisibleChanged(visible);
}

//  void QAbstractAxis::labelsAngleChanged(qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis18labelsAngleChangedEd(
    QAbstractAxis *self,
    qreal angle) {
  self->labelsAngleChanged(angle);
}

//  void QAbstractAxis::labelDelegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis20labelDelegateChangedEv(QAbstractAxis *self) {
  self->labelDelegateChanged();
}

//  void QAbstractAxis::gridVisibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis18gridVisibleChangedEb(
    QAbstractAxis *self,
    bool visible) {
  self->gridVisibleChanged(visible);
}

//  void QAbstractAxis::subGridVisibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis21subGridVisibleChangedEb(
    QAbstractAxis *self,
    bool visible) {
  self->subGridVisibleChanged(visible);
}

//  void QAbstractAxis::titleTextChanged(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis16titleTextChangedERK7QString(
    QAbstractAxis *self,
    const QString *title) {
  self->titleTextChanged(*title);
}

//  void QAbstractAxis::titleColorChanged(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis17titleColorChangedE6QColor(
    QAbstractAxis *self,
    const QColor *color) {
  self->titleColorChanged(*color);
}

//  void QAbstractAxis::titleVisibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis19titleVisibleChangedEb(
    QAbstractAxis *self,
    bool visible) {
  self->titleVisibleChanged(visible);
}

//  void QAbstractAxis::titleFontChanged(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis16titleFontChangedERK5QFont(
    QAbstractAxis *self,
    const QFont *font) {
  self->titleFontChanged(*font);
}

//  void QAbstractAxis::alignmentChanged(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis16alignmentChangedE6QFlagsIN2Qt13AlignmentFlagEE(
    QAbstractAxis *self,
    int alignment) {
  self->alignmentChanged(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void QAbstractAxis::textElideModeChanged(Qt::TextElideMode elideMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis20textElideModeChangedEN2Qt13TextElideModeE(
    QAbstractAxis *self,
    Qt::TextElideMode elideMode) {
  self->textElideModeChanged(elideMode);
}

//  void QAbstractAxis::subColorChanged(QColor newColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis15subColorChangedE6QColor(
    QAbstractAxis *self,
    const QColor *newColor) {
  self->subColorChanged(*newColor);
}

//  void QAbstractAxis::colorChanged(QColor newColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis12colorChangedE6QColor(
    QAbstractAxis *self,
    const QColor *newColor) {
  self->colorChanged(*newColor);
}

//  void QAbstractAxis::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis6updateEv(QAbstractAxis *self) {
  self->update();
}

//  void QAbstractAxis::rangeChanged(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis12rangeChangedEdd(
    QAbstractAxis *self,
    qreal min,
    qreal max) {
  self->rangeChanged(min, max);
}

//  a Python function taken by a CuteQAbstractAxis, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractAxis(
    QAbstractAxis *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractAxis *>(self)->take(key, call);
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom)))
