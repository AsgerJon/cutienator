//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qlegendmarker.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qlegendmarker.h>
#include <QtCore/qstring.h>
#include <QtGui/qbrush.h>
#include <QtGui/qfont.h>
#include <QtGui/qpen.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QLegendMarker that Python can take functions over in. Every QLegendMarker
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQLegendMarkerCall0)(const void *, int *);
typedef void * (*CuteQLegendMarkerCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLegendMarkerCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLegendMarkerCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendMarkerCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendMarkerCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendMarkerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendMarkerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendMarkerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLegendMarker : public QLegendMarker {
public:
  using QLegendMarker::QLegendMarker;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QLegendMarker4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QLegendMarker6seriesEv")) {
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

  //  LegendMarkerType QLegendMarker::type()
  QLegendMarker::LegendMarkerType type() override {
    if (taken[0]) {
      int handled = 0;
      CuteQLegendMarkerCall0 call = reinterpret_cast<CuteQLegendMarkerCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QLegendMarker::LegendMarkerType>(given);
    }
    return {};
  }

  //  QAbstractSeries *QLegendMarker::series()
  QAbstractSeries *series() override {
    if (taken[1]) {
      int handled = 0;
      CuteQLegendMarkerCall1 call = reinterpret_cast<CuteQLegendMarkerCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries *>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLegendMarkerCall2 call = reinterpret_cast<CuteQLegendMarkerCall2>(taken[2]);
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
      CuteQLegendMarkerCall3 call = reinterpret_cast<CuteQLegendMarkerCall3>(taken[3]);
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
      CuteQLegendMarkerCall4 call = reinterpret_cast<CuteQLegendMarkerCall4>(taken[4]);
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
      CuteQLegendMarkerCall5 call = reinterpret_cast<CuteQLegendMarkerCall5>(taken[5]);
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
      CuteQLegendMarkerCall6 call = reinterpret_cast<CuteQLegendMarkerCall6>(taken[6]);
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
      CuteQLegendMarkerCall7 call = reinterpret_cast<CuteQLegendMarkerCall7>(taken[7]);
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
      CuteQLegendMarkerCall8 call = reinterpret_cast<CuteQLegendMarkerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLegendMarker::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QLegendMarker10metaObjectEv(
    const QLegendMarker *self) {
  return self->metaObject();
}

//  void *QLegendMarker::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QLegendMarker11qt_metacastEPKc(
    QLegendMarker *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QLegendMarker::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QLegendMarker11qt_metacallEN11QMetaObject4CallEiPPv(
    QLegendMarker *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QLegendMarker::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QLegendMarker2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLegendMarker::tr(s, c, n));
}

//  QLegendMarker::~QLegendMarker()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLegendMarkerD1Ev(QLegendMarker *self) {
  delete self;
}

//  LegendMarkerType QLegendMarker::type()
extern "C" Q_DECL_EXPORT
QLegendMarker::LegendMarkerType ritual_ZN13QLegendMarker4typeEv(
    QLegendMarker *self) {
  return self->type();
}

//  QString QLegendMarker::label() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QLegendMarker5labelEv(const QLegendMarker *self) {
  return new QString(self->label());
}

//  void QLegendMarker::setLabel(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLegendMarker8setLabelERK7QString(
    QLegendMarker *self,
    const QString *label) {
  self->setLabel(*label);
}

//  QBrush QLegendMarker::labelBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK13QLegendMarker10labelBrushEv(const QLegendMarker *self) {
  return new QBrush(self->labelBrush());
}

//  void QLegendMarker::setLabelBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLegendMarker13setLabelBrushERK6QBrush(
    QLegendMarker *self,
    const QBrush *brush) {
  self->setLabelBrush(*brush);
}

//  QFont QLegendMarker::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK13QLegendMarker4fontEv(const QLegendMarker *self) {
  return new QFont(self->font());
}

//  void QLegendMarker::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLegendMarker7setFontERK5QFont(
    QLegendMarker *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QPen QLegendMarker::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK13QLegendMarker3penEv(const QLegendMarker *self) {
  return new QPen(self->pen());
}

//  void QLegendMarker::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLegendMarker6setPenERK4QPen(
    QLegendMarker *self,
    const QPen *pen) {
  self->setPen(*pen);
}

//  QBrush QLegendMarker::brush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK13QLegendMarker5brushEv(const QLegendMarker *self) {
  return new QBrush(self->brush());
}

//  void QLegendMarker::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLegendMarker8setBrushERK6QBrush(
    QLegendMarker *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  bool QLegendMarker::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLegendMarker9isVisibleEv(const QLegendMarker *self) {
  return self->isVisible();
}

//  void QLegendMarker::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLegendMarker10setVisibleEb(
    QLegendMarker *self,
    bool visible) {
  self->setVisible(visible);
}

//  QLegend::MarkerShape QLegendMarker::shape() const
extern "C" Q_DECL_EXPORT
QLegend::MarkerShape ritual_ZNK13QLegendMarker5shapeEv(
    const QLegendMarker *self) {
  return self->shape();
}

//  void QLegendMarker::setShape(QLegend::MarkerShape shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLegendMarker8setShapeEN7QLegend11MarkerShapeE(
    QLegendMarker *self,
    QLegend::MarkerShape shape) {
  self->setShape(shape);
}

//  QAbstractSeries *QLegendMarker::series()
extern "C" Q_DECL_EXPORT
QAbstractSeries *ritual_ZN13QLegendMarker6seriesEv(QLegendMarker *self) {
  return self->series();
}

//  void QLegendMarker::clicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLegendMarker7clickedEv(QLegendMarker *self) {
  self->clicked();
}

//  void QLegendMarker::hovered(bool status)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLegendMarker7hoveredEb(QLegendMarker *self, bool status) {
  self->hovered(status);
}

//  void QLegendMarker::labelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLegendMarker12labelChangedEv(QLegendMarker *self) {
  self->labelChanged();
}

//  void QLegendMarker::labelBrushChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLegendMarker17labelBrushChangedEv(QLegendMarker *self) {
  self->labelBrushChanged();
}

//  void QLegendMarker::fontChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLegendMarker11fontChangedEv(QLegendMarker *self) {
  self->fontChanged();
}

//  void QLegendMarker::penChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLegendMarker10penChangedEv(QLegendMarker *self) {
  self->penChanged();
}

//  void QLegendMarker::brushChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLegendMarker12brushChangedEv(QLegendMarker *self) {
  self->brushChanged();
}

//  void QLegendMarker::visibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLegendMarker14visibleChangedEv(QLegendMarker *self) {
  self->visibleChanged();
}

//  void QLegendMarker::shapeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLegendMarker12shapeChangedEv(QLegendMarker *self) {
  self->shapeChanged();
}

//  QLegendMarker::QLegendMarker(QLegendMarkerPrivate &d, QObject *parent)
extern "C" Q_DECL_EXPORT
QLegendMarker *ritual_ZN13QLegendMarkerC1ER20QLegendMarkerPrivateP7QObject(
    QLegendMarkerPrivate *d,
    QObject *parent) {
  return new CuteQLegendMarker(*d, parent);
}

//  a Python function taken by a CuteQLegendMarker, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLegendMarker(
    QLegendMarker *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLegendMarker *>(self)->take(key, call);
}

//  QList<QLegendMarker *>::QList()
extern "C" Q_DECL_EXPORT
QList<QLegendMarker *> *ritual_list_make_QLegendMarker_ptr() {
  return new QList<QLegendMarker *>();
}

//  void QList<QLegendMarker *>::append(const QLegendMarker * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QLegendMarker_ptr(
    QList<QLegendMarker *> *self,
    QLegendMarker *element) {
  self->append(element);
}

//  qsizetype QList<QLegendMarker *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QLegendMarker_ptr(
    const QList<QLegendMarker *> *self) {
  return self->size();
}

//  const QLegendMarker * &QList<QLegendMarker *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QLegendMarker *ritual_list_at_QLegendMarker_ptr(
    const QList<QLegendMarker *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QLegendMarker *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QLegendMarker_ptr(QList<QLegendMarker *> *self) {
  delete self;
}
