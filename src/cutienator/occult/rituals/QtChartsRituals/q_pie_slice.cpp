//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qpieslice.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qpieslice.h>
#include <QtCore/qstring.h>
#include <QtGui/qpen.h>
#include <QtGui/qcolor.h>
#include <QtGui/qbrush.h>
#include <QtGui/qfont.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QPieSlice that Python can take functions over in. Every QPieSlice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPieSliceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPieSliceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSliceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSliceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSliceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSliceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSliceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPieSlice : public QPieSlice {
public:
  using QPieSlice::QPieSlice;
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
      CuteQPieSliceCall0 call = reinterpret_cast<CuteQPieSliceCall0>(taken[0]);
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
      CuteQPieSliceCall1 call = reinterpret_cast<CuteQPieSliceCall1>(taken[1]);
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
      CuteQPieSliceCall2 call = reinterpret_cast<CuteQPieSliceCall2>(taken[2]);
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
      CuteQPieSliceCall3 call = reinterpret_cast<CuteQPieSliceCall3>(taken[3]);
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
      CuteQPieSliceCall4 call = reinterpret_cast<CuteQPieSliceCall4>(taken[4]);
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
      CuteQPieSliceCall5 call = reinterpret_cast<CuteQPieSliceCall5>(taken[5]);
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
      CuteQPieSliceCall6 call = reinterpret_cast<CuteQPieSliceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPieSlice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QPieSlice10metaObjectEv(
    const QPieSlice *self) {
  return self->metaObject();
}

//  QString QPieSlice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QPieSlice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPieSlice::tr(s, c, n));
}

//  QPieSlice::QPieSlice(QObject *parent)
extern "C" Q_DECL_EXPORT
QPieSlice *ritual_ZN9QPieSliceC1EP7QObject(QObject *parent) {
  return new CuteQPieSlice(parent);
}

//  QPieSlice::QPieSlice(QString label, qreal value, QObject *parent)
extern "C" Q_DECL_EXPORT
QPieSlice *ritual_ZN9QPieSliceC1E7QStringdP7QObject(
    const QString *label,
    qreal value,
    QObject *parent) {
  return new CuteQPieSlice(*label, value, parent);
}

//  QPieSlice::~QPieSlice()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPieSliceD1Ev(QPieSlice *self) {
  delete self;
}

//  void QPieSlice::setLabel(QString label)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPieSlice8setLabelE7QString(
    QPieSlice *self,
    const QString *label) {
  self->setLabel(*label);
}

//  QString QPieSlice::label() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QPieSlice5labelEv(const QPieSlice *self) {
  return new QString(self->label());
}

//  void QPieSlice::setValue(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPieSlice8setValueEd(QPieSlice *self, qreal value) {
  self->setValue(value);
}

//  qreal QPieSlice::value() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QPieSlice5valueEv(const QPieSlice *self) {
  return self->value();
}

//  void QPieSlice::setLabelVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPieSlice15setLabelVisibleEb(QPieSlice *self, bool visible) {
  self->setLabelVisible(visible);
}

//  bool QPieSlice::isLabelVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QPieSlice14isLabelVisibleEv(const QPieSlice *self) {
  return self->isLabelVisible();
}

//  LabelPosition QPieSlice::labelPosition()
extern "C" Q_DECL_EXPORT
QPieSlice::LabelPosition ritual_ZN9QPieSlice13labelPositionEv(
    QPieSlice *self) {
  return self->labelPosition();
}

//  void QPieSlice::setLabelPosition(LabelPosition position)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPieSlice16setLabelPositionENS_13LabelPositionE(
    QPieSlice *self,
    QPieSlice::LabelPosition position) {
  self->setLabelPosition(position);
}

//  void QPieSlice::setExploded(bool exploded)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPieSlice11setExplodedEb(QPieSlice *self, bool exploded) {
  self->setExploded(exploded);
}

//  bool QPieSlice::isExploded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QPieSlice10isExplodedEv(const QPieSlice *self) {
  return self->isExploded();
}

//  void QPieSlice::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPieSlice6setPenERK4QPen(QPieSlice *self, const QPen *pen) {
  self->setPen(*pen);
}

//  QPen QPieSlice::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK9QPieSlice3penEv(const QPieSlice *self) {
  return new QPen(self->pen());
}

//  QColor QPieSlice::borderColor()
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN9QPieSlice11borderColorEv(QPieSlice *self) {
  return new QColor(self->borderColor());
}

//  void QPieSlice::setBorderColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPieSlice14setBorderColorE6QColor(
    QPieSlice *self,
    const QColor *color) {
  self->setBorderColor(*color);
}

//  int QPieSlice::borderWidth()
extern "C" Q_DECL_EXPORT
int ritual_ZN9QPieSlice11borderWidthEv(QPieSlice *self) {
  return self->borderWidth();
}

//  void QPieSlice::setBorderWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPieSlice14setBorderWidthEi(QPieSlice *self, int width) {
  self->setBorderWidth(width);
}

//  void QPieSlice::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPieSlice8setBrushERK6QBrush(
    QPieSlice *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  QBrush QPieSlice::brush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK9QPieSlice5brushEv(const QPieSlice *self) {
  return new QBrush(self->brush());
}

//  QColor QPieSlice::color()
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN9QPieSlice5colorEv(QPieSlice *self) {
  return new QColor(self->color());
}

//  void QPieSlice::setColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPieSlice8setColorE6QColor(
    QPieSlice *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QPieSlice::setLabelBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPieSlice13setLabelBrushERK6QBrush(
    QPieSlice *self,
    const QBrush *brush) {
  self->setLabelBrush(*brush);
}

//  QBrush QPieSlice::labelBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK9QPieSlice10labelBrushEv(const QPieSlice *self) {
  return new QBrush(self->labelBrush());
}

//  QColor QPieSlice::labelColor()
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN9QPieSlice10labelColorEv(QPieSlice *self) {
  return new QColor(self->labelColor());
}

//  void QPieSlice::setLabelColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPieSlice13setLabelColorE6QColor(
    QPieSlice *self,
    const QColor *color) {
  self->setLabelColor(*color);
}

//  void QPieSlice::setLabelFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPieSlice12setLabelFontERK5QFont(
    QPieSlice *self,
    const QFont *font) {
  self->setLabelFont(*font);
}

//  QFont QPieSlice::labelFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK9QPieSlice9labelFontEv(const QPieSlice *self) {
  return new QFont(self->labelFont());
}

//  void QPieSlice::setLabelArmLengthFactor(qreal factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPieSlice23setLabelArmLengthFactorEd(
    QPieSlice *self,
    qreal factor) {
  self->setLabelArmLengthFactor(factor);
}

//  qreal QPieSlice::labelArmLengthFactor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QPieSlice20labelArmLengthFactorEv(const QPieSlice *self) {
  return self->labelArmLengthFactor();
}

//  void QPieSlice::setExplodeDistanceFactor(qreal factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPieSlice24setExplodeDistanceFactorEd(
    QPieSlice *self,
    qreal factor) {
  self->setExplodeDistanceFactor(factor);
}

//  qreal QPieSlice::explodeDistanceFactor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QPieSlice21explodeDistanceFactorEv(const QPieSlice *self) {
  return self->explodeDistanceFactor();
}

//  qreal QPieSlice::percentage() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QPieSlice10percentageEv(const QPieSlice *self) {
  return self->percentage();
}

//  qreal QPieSlice::startAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QPieSlice10startAngleEv(const QPieSlice *self) {
  return self->startAngle();
}

//  qreal QPieSlice::angleSpan() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QPieSlice9angleSpanEv(const QPieSlice *self) {
  return self->angleSpan();
}

//  QPieSeries *QPieSlice::series() const
extern "C" Q_DECL_EXPORT
QPieSeries *ritual_ZNK9QPieSlice6seriesEv(const QPieSlice *self) {
  return self->series();
}

//  QPieSlicePrivate *QPieSlice::d_func()
extern "C" Q_DECL_EXPORT
QPieSlicePrivate *ritual_ZN9QPieSlice6d_funcEv(QPieSlice *self) {
  return self->d_func();
}

//  const QPieSlicePrivate *QPieSlice::d_func() const
extern "C" Q_DECL_EXPORT
const QPieSlicePrivate *ritual_ZNK9QPieSlice6d_funcEv(
    const QPieSlice *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQPieSlice, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPieSlice(QPieSlice *self, const char *key, void *call) {
  return static_cast<CuteQPieSlice *>(self)->take(key, call);
}

//  QList<QPieSlice *>::QList()
extern "C" Q_DECL_EXPORT
QList<QPieSlice *> *ritual_list_make_QPieSlice_ptr() {
  return new QList<QPieSlice *>();
}

//  void QList<QPieSlice *>::append(const QPieSlice * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QPieSlice_ptr(
    QList<QPieSlice *> *self,
    QPieSlice *element) {
  self->append(element);
}

//  qsizetype QList<QPieSlice *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QPieSlice_ptr(const QList<QPieSlice *> *self) {
  return self->size();
}

//  const QPieSlice * &QList<QPieSlice *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QPieSlice *ritual_list_at_QPieSlice_ptr(
    const QList<QPieSlice *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QPieSlice *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QPieSlice_ptr(QList<QPieSlice *> *self) {
  delete self;
}
