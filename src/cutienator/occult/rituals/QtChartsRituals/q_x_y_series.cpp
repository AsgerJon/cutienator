//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qxyseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qxyseries.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpen.h>
#include <QtGui/qbrush.h>
#include <QtGui/qcolor.h>
#include <QtGui/qfont.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QXYSeries that Python can take functions over in. Every QXYSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQXYSeriesCall0)(const void *, const QPen *, int *);
typedef void (*CuteQXYSeriesCall1)(const void *, const QBrush *, int *);
typedef void (*CuteQXYSeriesCall2)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQXYSeriesCall3)(const void *, int *);
typedef int (*CuteQXYSeriesCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQXYSeriesCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQXYSeriesCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYSeriesCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYSeriesCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYSeriesCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYSeriesCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYSeriesCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQXYSeries : public QXYSeries {
public:
  using QXYSeries::QXYSeries;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QXYSeries6setPenERK4QPen")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QXYSeries8setBrushERK6QBrush")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QXYSeries8setColorERK6QColor")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QXYSeries5colorEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QAbstractSeries4typeEv")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QXYSeries::setPen(const QPen &pen)
  void setPen(const QPen &pen) override {
    if (taken[0]) {
      int handled = 0;
      CuteQXYSeriesCall0 call = reinterpret_cast<CuteQXYSeriesCall0>(taken[0]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    QXYSeries::setPen(pen);
  }

  //  void QXYSeries::setBrush(const QBrush &brush)
  void setBrush(const QBrush &brush) override {
    if (taken[1]) {
      int handled = 0;
      CuteQXYSeriesCall1 call = reinterpret_cast<CuteQXYSeriesCall1>(taken[1]);
      call(this, &brush, &handled);
      if (handled) return;
    }
    QXYSeries::setBrush(brush);
  }

  //  void QXYSeries::setColor(const QColor &color)
  void setColor(const QColor &color) override {
    if (taken[2]) {
      int handled = 0;
      CuteQXYSeriesCall2 call = reinterpret_cast<CuteQXYSeriesCall2>(taken[2]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QXYSeries::setColor(color);
  }

  //  QColor QXYSeries::color() const
  QColor color() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQXYSeriesCall3 call = reinterpret_cast<CuteQXYSeriesCall3>(taken[3]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QXYSeries::color();
  }

  //  SeriesType QAbstractSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQXYSeriesCall4 call = reinterpret_cast<CuteQXYSeriesCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQXYSeriesCall5 call = reinterpret_cast<CuteQXYSeriesCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQXYSeriesCall6 call = reinterpret_cast<CuteQXYSeriesCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQXYSeriesCall7 call = reinterpret_cast<CuteQXYSeriesCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQXYSeriesCall8 call = reinterpret_cast<CuteQXYSeriesCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQXYSeriesCall9 call = reinterpret_cast<CuteQXYSeriesCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQXYSeriesCall10 call = reinterpret_cast<CuteQXYSeriesCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQXYSeriesCall11 call = reinterpret_cast<CuteQXYSeriesCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QXYSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QXYSeries10metaObjectEv(
    const QXYSeries *self) {
  return self->metaObject();
}

//  QString QXYSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QXYSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QXYSeries::tr(s, c, n));
}

//  QXYSeries::~QXYSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeriesD1Ev(QXYSeries *self) {
  delete self;
}

//  void QXYSeries::append(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries6appendEdd(QXYSeries *self, qreal x, qreal y) {
  self->append(x, y);
}

//  void QXYSeries::append(const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries6appendERK7QPointF(
    QXYSeries *self,
    const QPointF *point) {
  self->append(*point);
}

//  void QXYSeries::append(const QList<QPointF> &points)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries6appendERK5QListI7QPointFE(
    QXYSeries *self,
    const QList<QPointF> *points) {
  self->append(*points);
}

//  void QXYSeries::replace(qreal oldX, qreal oldY, qreal newX, qreal newY)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries7replaceEdddd(
    QXYSeries *self,
    qreal oldX,
    qreal oldY,
    qreal newX,
    qreal newY) {
  self->replace(oldX, oldY, newX, newY);
}

//  void QXYSeries::replace(const QPointF &oldPoint, const QPointF &newPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries7replaceERK7QPointFS2_(
    QXYSeries *self,
    const QPointF *oldPoint,
    const QPointF *newPoint) {
  self->replace(*oldPoint, *newPoint);
}

//  void QXYSeries::replace(int index, qreal newX, qreal newY)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries7replaceEidd(
    QXYSeries *self,
    int index,
    qreal newX,
    qreal newY) {
  self->replace(index, newX, newY);
}

//  void QXYSeries::replace(int index, const QPointF &newPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries7replaceEiRK7QPointF(
    QXYSeries *self,
    int index,
    const QPointF *newPoint) {
  self->replace(index, *newPoint);
}

//  void QXYSeries::remove(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries6removeEdd(QXYSeries *self, qreal x, qreal y) {
  self->remove(x, y);
}

//  void QXYSeries::remove(const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries6removeERK7QPointF(
    QXYSeries *self,
    const QPointF *point) {
  self->remove(*point);
}

//  void QXYSeries::remove(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries6removeEi(QXYSeries *self, int index) {
  self->remove(index);
}

//  void QXYSeries::removePoints(int index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries12removePointsEii(
    QXYSeries *self,
    int index,
    int count) {
  self->removePoints(index, count);
}

//  void QXYSeries::insert(int index, const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries6insertEiRK7QPointF(
    QXYSeries *self,
    int index,
    const QPointF *point) {
  self->insert(index, *point);
}

//  void QXYSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries5clearEv(QXYSeries *self) {
  self->clear();
}

//  int QXYSeries::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QXYSeries5countEv(const QXYSeries *self) {
  return self->count();
}

//  QList<QPointF> QXYSeries::points() const
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_ZNK9QXYSeries6pointsEv(const QXYSeries *self) {
  return new QList<QPointF>(self->points());
}

#if QT_DEPRECATED_SINCE(6, 0)
//  QList<QPointF> QXYSeries::pointsVector() const
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_ZNK9QXYSeries12pointsVectorEv(const QXYSeries *self) {
  return new QList<QPointF>(self->pointsVector());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  const QPointF &QXYSeries::at(int index) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK9QXYSeries2atEi(const QXYSeries *self, int index) {
  return new QPointF(self->at(index));
}

//  void QXYSeries::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries6setPenERK4QPen(QXYSeries *self, const QPen *pen) {
  self->setPen(*pen);
}

//  QPen QXYSeries::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK9QXYSeries3penEv(const QXYSeries *self) {
  return new QPen(self->pen());
}

//  void QXYSeries::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries8setBrushERK6QBrush(
    QXYSeries *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  QBrush QXYSeries::brush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK9QXYSeries5brushEv(const QXYSeries *self) {
  return new QBrush(self->brush());
}

//  void QXYSeries::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries8setColorERK6QColor(
    QXYSeries *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QColor QXYSeries::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK9QXYSeries5colorEv(const QXYSeries *self) {
  return new QColor(self->color());
}

//  void QXYSeries::setSelectedColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries16setSelectedColorERK6QColor(
    QXYSeries *self,
    const QColor *color) {
  self->setSelectedColor(*color);
}

//  QColor QXYSeries::selectedColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK9QXYSeries13selectedColorEv(const QXYSeries *self) {
  return new QColor(self->selectedColor());
}

//  void QXYSeries::setPointsVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries16setPointsVisibleEb(QXYSeries *self, bool visible) {
  self->setPointsVisible(visible);
}

//  bool QXYSeries::pointsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QXYSeries13pointsVisibleEv(const QXYSeries *self) {
  return self->pointsVisible();
}

//  void QXYSeries::setPointLabelsFormat(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries20setPointLabelsFormatERK7QString(
    QXYSeries *self,
    const QString *format) {
  self->setPointLabelsFormat(*format);
}

//  QString QXYSeries::pointLabelsFormat() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QXYSeries17pointLabelsFormatEv(const QXYSeries *self) {
  return new QString(self->pointLabelsFormat());
}

//  void QXYSeries::setPointLabelsVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries21setPointLabelsVisibleEb(
    QXYSeries *self,
    bool visible) {
  self->setPointLabelsVisible(visible);
}

//  bool QXYSeries::pointLabelsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QXYSeries18pointLabelsVisibleEv(const QXYSeries *self) {
  return self->pointLabelsVisible();
}

//  void QXYSeries::setPointLabelsFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries18setPointLabelsFontERK5QFont(
    QXYSeries *self,
    const QFont *font) {
  self->setPointLabelsFont(*font);
}

//  QFont QXYSeries::pointLabelsFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK9QXYSeries15pointLabelsFontEv(const QXYSeries *self) {
  return new QFont(self->pointLabelsFont());
}

//  void QXYSeries::setPointLabelsColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries19setPointLabelsColorERK6QColor(
    QXYSeries *self,
    const QColor *color) {
  self->setPointLabelsColor(*color);
}

//  QColor QXYSeries::pointLabelsColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK9QXYSeries16pointLabelsColorEv(const QXYSeries *self) {
  return new QColor(self->pointLabelsColor());
}

//  void QXYSeries::setPointLabelsClipping(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries22setPointLabelsClippingEb(
    QXYSeries *self,
    bool enabled) {
  self->setPointLabelsClipping(enabled);
}

//  bool QXYSeries::pointLabelsClipping() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QXYSeries19pointLabelsClippingEv(const QXYSeries *self) {
  return self->pointLabelsClipping();
}

//  void QXYSeries::replace(const QList<QPointF> &points)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries7replaceERK5QListI7QPointFE(
    QXYSeries *self,
    const QList<QPointF> *points) {
  self->replace(*points);
}

//  bool QXYSeries::isPointSelected(int index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QXYSeries15isPointSelectedEi(QXYSeries *self, int index) {
  return self->isPointSelected(index);
}

//  void QXYSeries::selectPoint(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries11selectPointEi(QXYSeries *self, int index) {
  self->selectPoint(index);
}

//  void QXYSeries::deselectPoint(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries13deselectPointEi(QXYSeries *self, int index) {
  self->deselectPoint(index);
}

//  void QXYSeries::setPointSelected(int index, bool selected)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries16setPointSelectedEib(
    QXYSeries *self,
    int index,
    bool selected) {
  self->setPointSelected(index, selected);
}

//  void QXYSeries::selectAllPoints()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries15selectAllPointsEv(QXYSeries *self) {
  self->selectAllPoints();
}

//  void QXYSeries::deselectAllPoints()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries17deselectAllPointsEv(QXYSeries *self) {
  self->deselectAllPoints();
}

//  void QXYSeries::setLightMarker(const QImage &lightMarker)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries14setLightMarkerERK6QImage(
    QXYSeries *self,
    const QImage *lightMarker) {
  self->setLightMarker(*lightMarker);
}

//  const QImage &QXYSeries::lightMarker() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK9QXYSeries11lightMarkerEv(const QXYSeries *self) {
  return new QImage(self->lightMarker());
}

//  void QXYSeries::setSelectedLightMarker(const QImage &selectedLightMarker)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries22setSelectedLightMarkerERK6QImage(
    QXYSeries *self,
    const QImage *selectedLightMarker) {
  self->setSelectedLightMarker(*selectedLightMarker);
}

//  const QImage &QXYSeries::selectedLightMarker() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK9QXYSeries19selectedLightMarkerEv(const QXYSeries *self) {
  return new QImage(self->selectedLightMarker());
}

//  void QXYSeries::setMarkerSize(qreal size)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries13setMarkerSizeEd(QXYSeries *self, qreal size) {
  self->setMarkerSize(size);
}

//  qreal QXYSeries::markerSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QXYSeries10markerSizeEv(const QXYSeries *self) {
  return self->markerSize();
}

//  void QXYSeries::setBestFitLineVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries21setBestFitLineVisibleEb(
    QXYSeries *self,
    bool visible) {
  self->setBestFitLineVisible(visible);
}

//  bool QXYSeries::bestFitLineVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QXYSeries18bestFitLineVisibleEv(const QXYSeries *self) {
  return self->bestFitLineVisible();
}

//  void QXYSeries::setBestFitLinePen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries17setBestFitLinePenERK4QPen(
    QXYSeries *self,
    const QPen *pen) {
  self->setBestFitLinePen(*pen);
}

//  QPen QXYSeries::bestFitLinePen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK9QXYSeries14bestFitLinePenEv(const QXYSeries *self) {
  return new QPen(self->bestFitLinePen());
}

//  void QXYSeries::setBestFitLineColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries19setBestFitLineColorERK6QColor(
    QXYSeries *self,
    const QColor *color) {
  self->setBestFitLineColor(*color);
}

//  QColor QXYSeries::bestFitLineColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK9QXYSeries16bestFitLineColorEv(const QXYSeries *self) {
  return new QColor(self->bestFitLineColor());
}

//  void QXYSeries::clearPointConfiguration(const int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries23clearPointConfigurationEi(
    QXYSeries *self,
    int index) {
  self->clearPointConfiguration(index);
}

//  void QXYSeries::clearPointsConfiguration()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries24clearPointsConfigurationEv(QXYSeries *self) {
  self->clearPointsConfiguration();
}

//  QXYSeriesPrivate *QXYSeries::d_func()
extern "C" Q_DECL_EXPORT
QXYSeriesPrivate *ritual_ZN9QXYSeries6d_funcEv(QXYSeries *self) {
  return self->d_func();
}

//  const QXYSeriesPrivate *QXYSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QXYSeriesPrivate *ritual_ZNK9QXYSeries6d_funcEv(
    const QXYSeries *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQXYSeries, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXYSeries(QXYSeries *self, const char *key, void *call) {
  return static_cast<CuteQXYSeries *>(self)->take(key, call);
}

//  void QXYSeries::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QXYSeries6setPenERK4QPen(
    QXYSeries *self,
    const QPen *pen) {
  self->QXYSeries::setPen(*pen);
}

//  void QXYSeries::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QXYSeries8setBrushERK6QBrush(
    QXYSeries *self,
    const QBrush *brush) {
  self->QXYSeries::setBrush(*brush);
}

//  void QXYSeries::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QXYSeries8setColorERK6QColor(
    QXYSeries *self,
    const QColor *color) {
  self->QXYSeries::setColor(*color);
}

//  QColor QXYSeries::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_own_ZNK9QXYSeries5colorEv(const QXYSeries *self) {
  return new QColor(self->QXYSeries::color());
}
