//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qabstractaxis.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qabstractaxis.h>
#include <QtCore/qstring.h>
#include <QtGui/qpen.h>
#include <QtGui/qcolor.h>
#include <QtGui/qbrush.h>
#include <QtGui/qfont.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
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

//  QString QAbstractAxis::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QAbstractAxis2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractAxis::tr(s, c, n));
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

//  void QAbstractAxis::setLinePen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis10setLinePenERK4QPen(
    QAbstractAxis *self,
    const QPen *pen) {
  self->setLinePen(*pen);
}

//  QPen QAbstractAxis::linePen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK13QAbstractAxis7linePenEv(const QAbstractAxis *self) {
  return new QPen(self->linePen());
}

//  void QAbstractAxis::setLinePenColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis15setLinePenColorE6QColor(
    QAbstractAxis *self,
    const QColor *color) {
  self->setLinePenColor(*color);
}

//  QColor QAbstractAxis::linePenColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK13QAbstractAxis12linePenColorEv(
    const QAbstractAxis *self) {
  return new QColor(self->linePenColor());
}

//  bool QAbstractAxis::isGridLineVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QAbstractAxis17isGridLineVisibleEv(
    const QAbstractAxis *self) {
  return self->isGridLineVisible();
}

//  void QAbstractAxis::setGridLineVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis18setGridLineVisibleEb(
    QAbstractAxis *self,
    bool visible) {
  self->setGridLineVisible(visible);
}

//  void QAbstractAxis::setGridLinePen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis14setGridLinePenERK4QPen(
    QAbstractAxis *self,
    const QPen *pen) {
  self->setGridLinePen(*pen);
}

//  QPen QAbstractAxis::gridLinePen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK13QAbstractAxis11gridLinePenEv(const QAbstractAxis *self) {
  return new QPen(self->gridLinePen());
}

//  bool QAbstractAxis::isMinorGridLineVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QAbstractAxis22isMinorGridLineVisibleEv(
    const QAbstractAxis *self) {
  return self->isMinorGridLineVisible();
}

//  void QAbstractAxis::setMinorGridLineVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis23setMinorGridLineVisibleEb(
    QAbstractAxis *self,
    bool visible) {
  self->setMinorGridLineVisible(visible);
}

//  void QAbstractAxis::setMinorGridLinePen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis19setMinorGridLinePenERK4QPen(
    QAbstractAxis *self,
    const QPen *pen) {
  self->setMinorGridLinePen(*pen);
}

//  QPen QAbstractAxis::minorGridLinePen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK13QAbstractAxis16minorGridLinePenEv(
    const QAbstractAxis *self) {
  return new QPen(self->minorGridLinePen());
}

//  void QAbstractAxis::setGridLineColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis16setGridLineColorERK6QColor(
    QAbstractAxis *self,
    const QColor *color) {
  self->setGridLineColor(*color);
}

//  QColor QAbstractAxis::gridLineColor()
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN13QAbstractAxis13gridLineColorEv(QAbstractAxis *self) {
  return new QColor(self->gridLineColor());
}

//  void QAbstractAxis::setMinorGridLineColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis21setMinorGridLineColorERK6QColor(
    QAbstractAxis *self,
    const QColor *color) {
  self->setMinorGridLineColor(*color);
}

//  QColor QAbstractAxis::minorGridLineColor()
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN13QAbstractAxis18minorGridLineColorEv(QAbstractAxis *self) {
  return new QColor(self->minorGridLineColor());
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

//  void QAbstractAxis::setLabelsBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis14setLabelsBrushERK6QBrush(
    QAbstractAxis *self,
    const QBrush *brush) {
  self->setLabelsBrush(*brush);
}

//  QBrush QAbstractAxis::labelsBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK13QAbstractAxis11labelsBrushEv(const QAbstractAxis *self) {
  return new QBrush(self->labelsBrush());
}

//  void QAbstractAxis::setLabelsFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis13setLabelsFontERK5QFont(
    QAbstractAxis *self,
    const QFont *font) {
  self->setLabelsFont(*font);
}

//  QFont QAbstractAxis::labelsFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK13QAbstractAxis10labelsFontEv(const QAbstractAxis *self) {
  return new QFont(self->labelsFont());
}

//  void QAbstractAxis::setLabelsAngle(int angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis14setLabelsAngleEi(
    QAbstractAxis *self,
    int angle) {
  self->setLabelsAngle(angle);
}

//  int QAbstractAxis::labelsAngle() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QAbstractAxis11labelsAngleEv(const QAbstractAxis *self) {
  return self->labelsAngle();
}

//  void QAbstractAxis::setLabelsColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis14setLabelsColorE6QColor(
    QAbstractAxis *self,
    const QColor *color) {
  self->setLabelsColor(*color);
}

//  QColor QAbstractAxis::labelsColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK13QAbstractAxis11labelsColorEv(const QAbstractAxis *self) {
  return new QColor(self->labelsColor());
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

//  void QAbstractAxis::setTitleBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis13setTitleBrushERK6QBrush(
    QAbstractAxis *self,
    const QBrush *brush) {
  self->setTitleBrush(*brush);
}

//  QBrush QAbstractAxis::titleBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK13QAbstractAxis10titleBrushEv(const QAbstractAxis *self) {
  return new QBrush(self->titleBrush());
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

//  bool QAbstractAxis::shadesVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QAbstractAxis13shadesVisibleEv(const QAbstractAxis *self) {
  return self->shadesVisible();
}

//  void QAbstractAxis::setShadesVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis16setShadesVisibleEb(
    QAbstractAxis *self,
    bool visible) {
  self->setShadesVisible(visible);
}

//  void QAbstractAxis::setShadesPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis12setShadesPenERK4QPen(
    QAbstractAxis *self,
    const QPen *pen) {
  self->setShadesPen(*pen);
}

//  QPen QAbstractAxis::shadesPen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK13QAbstractAxis9shadesPenEv(const QAbstractAxis *self) {
  return new QPen(self->shadesPen());
}

//  void QAbstractAxis::setShadesBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis14setShadesBrushERK6QBrush(
    QAbstractAxis *self,
    const QBrush *brush) {
  self->setShadesBrush(*brush);
}

//  QBrush QAbstractAxis::shadesBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK13QAbstractAxis11shadesBrushEv(const QAbstractAxis *self) {
  return new QBrush(self->shadesBrush());
}

//  void QAbstractAxis::setShadesColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis14setShadesColorE6QColor(
    QAbstractAxis *self,
    const QColor *color) {
  self->setShadesColor(*color);
}

//  QColor QAbstractAxis::shadesColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK13QAbstractAxis11shadesColorEv(const QAbstractAxis *self) {
  return new QColor(self->shadesColor());
}

//  void QAbstractAxis::setShadesBorderColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis20setShadesBorderColorE6QColor(
    QAbstractAxis *self,
    const QColor *color) {
  self->setShadesBorderColor(*color);
}

//  QColor QAbstractAxis::shadesBorderColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK13QAbstractAxis17shadesBorderColorEv(
    const QAbstractAxis *self) {
  return new QColor(self->shadesBorderColor());
}

//  Qt::Orientation QAbstractAxis::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK13QAbstractAxis11orientationEv(
    const QAbstractAxis *self) {
  return self->orientation();
}

//  Qt::Alignment QAbstractAxis::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QAbstractAxis9alignmentEv(const QAbstractAxis *self) {
  return static_cast<int>(self->alignment().toInt());
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

//  void QAbstractAxis::setReverse(bool reverse)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis10setReverseEb(
    QAbstractAxis *self,
    bool reverse) {
  self->setReverse(reverse);
}

//  bool QAbstractAxis::isReverse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QAbstractAxis9isReverseEv(const QAbstractAxis *self) {
  return self->isReverse();
}

//  void QAbstractAxis::setLabelsEditable(bool editable)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis17setLabelsEditableEb(
    QAbstractAxis *self,
    bool editable) {
  self->setLabelsEditable(editable);
}

//  bool QAbstractAxis::labelsEditable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QAbstractAxis14labelsEditableEv(const QAbstractAxis *self) {
  return self->labelsEditable();
}

//  bool QAbstractAxis::labelsTruncated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QAbstractAxis15labelsTruncatedEv(
    const QAbstractAxis *self) {
  return self->labelsTruncated();
}

//  void QAbstractAxis::setTruncateLabels(bool truncateLabels)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAbstractAxis17setTruncateLabelsEb(
    QAbstractAxis *self,
    bool truncateLabels) {
  self->setTruncateLabels(truncateLabels);
}

//  bool QAbstractAxis::truncateLabels() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QAbstractAxis14truncateLabelsEv(const QAbstractAxis *self) {
  return self->truncateLabels();
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

//  QList<QAbstractAxis *>::QList()
extern "C" Q_DECL_EXPORT
QList<QAbstractAxis *> *ritual_list_make_QAbstractAxis_ptr() {
  return new QList<QAbstractAxis *>();
}

//  void QList<QAbstractAxis *>::append(const QAbstractAxis * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QAbstractAxis_ptr(
    QList<QAbstractAxis *> *self,
    QAbstractAxis *element) {
  self->append(element);
}

//  qsizetype QList<QAbstractAxis *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QAbstractAxis_ptr(
    const QList<QAbstractAxis *> *self) {
  return self->size();
}

//  const QAbstractAxis * &QList<QAbstractAxis *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_list_at_QAbstractAxis_ptr(
    const QList<QAbstractAxis *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QAbstractAxis *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QAbstractAxis_ptr(QList<QAbstractAxis *> *self) {
  delete self;
}
