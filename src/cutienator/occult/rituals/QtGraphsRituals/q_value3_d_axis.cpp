//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qvalue3daxis.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qvalue3daxis.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QValue3DAxis that Python can take functions over in. Every QValue3DAxis
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQValue3DAxisCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQValue3DAxisCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQValue3DAxis : public QValue3DAxis {
public:
  using QValue3DAxis::QValue3DAxis;
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
      CuteQValue3DAxisCall0 call = reinterpret_cast<CuteQValue3DAxisCall0>(taken[0]);
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
      CuteQValue3DAxisCall1 call = reinterpret_cast<CuteQValue3DAxisCall1>(taken[1]);
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
      CuteQValue3DAxisCall2 call = reinterpret_cast<CuteQValue3DAxisCall2>(taken[2]);
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
      CuteQValue3DAxisCall3 call = reinterpret_cast<CuteQValue3DAxisCall3>(taken[3]);
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
      CuteQValue3DAxisCall4 call = reinterpret_cast<CuteQValue3DAxisCall4>(taken[4]);
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
      CuteQValue3DAxisCall5 call = reinterpret_cast<CuteQValue3DAxisCall5>(taken[5]);
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
      CuteQValue3DAxisCall6 call = reinterpret_cast<CuteQValue3DAxisCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QValue3DAxis::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QValue3DAxis10metaObjectEv(
    const QValue3DAxis *self) {
  return self->metaObject();
}

//  void *QValue3DAxis::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QValue3DAxis11qt_metacastEPKc(
    QValue3DAxis *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QValue3DAxis::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QValue3DAxis11qt_metacallEN11QMetaObject4CallEiPPv(
    QValue3DAxis *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QValue3DAxis::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QValue3DAxis2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QValue3DAxis::tr(s, c, n));
}

//  QValue3DAxisPrivate *QValue3DAxis::d_func()
extern "C" Q_DECL_EXPORT
QValue3DAxisPrivate *ritual_ZN12QValue3DAxis6d_funcEv(QValue3DAxis *self) {
  return self->d_func();
}

//  const QValue3DAxisPrivate *QValue3DAxis::d_func() const
extern "C" Q_DECL_EXPORT
const QValue3DAxisPrivate *ritual_ZNK12QValue3DAxis6d_funcEv(
    const QValue3DAxis *self) {
  return self->d_func();
}

//  QValue3DAxis::QValue3DAxis(QObject *parent)
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZN12QValue3DAxisC1EP7QObject(QObject *parent) {
  return new CuteQValue3DAxis(parent);
}

//  QValue3DAxis::~QValue3DAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QValue3DAxisD1Ev(QValue3DAxis *self) {
  delete self;
}

//  void QValue3DAxis::setSegmentCount(qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QValue3DAxis15setSegmentCountEx(
    QValue3DAxis *self,
    qsizetype count) {
  self->setSegmentCount(count);
}

//  qsizetype QValue3DAxis::segmentCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK12QValue3DAxis12segmentCountEv(
    const QValue3DAxis *self) {
  return self->segmentCount();
}

//  void QValue3DAxis::setSubSegmentCount(qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QValue3DAxis18setSubSegmentCountEx(
    QValue3DAxis *self,
    qsizetype count) {
  self->setSubSegmentCount(count);
}

//  qsizetype QValue3DAxis::subSegmentCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK12QValue3DAxis15subSegmentCountEv(
    const QValue3DAxis *self) {
  return self->subSegmentCount();
}

//  void QValue3DAxis::setLabelFormat(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QValue3DAxis14setLabelFormatERK7QString(
    QValue3DAxis *self,
    const QString *format) {
  self->setLabelFormat(*format);
}

//  QString QValue3DAxis::labelFormat() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QValue3DAxis11labelFormatEv(const QValue3DAxis *self) {
  return new QString(self->labelFormat());
}

//  void QValue3DAxis::setFormatter(QValue3DAxisFormatter *formatter)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QValue3DAxis12setFormatterEP21QValue3DAxisFormatter(
    QValue3DAxis *self,
    QValue3DAxisFormatter *formatter) {
  self->setFormatter(formatter);
}

//  QValue3DAxisFormatter *QValue3DAxis::formatter() const
extern "C" Q_DECL_EXPORT
QValue3DAxisFormatter *ritual_ZNK12QValue3DAxis9formatterEv(
    const QValue3DAxis *self) {
  return self->formatter();
}

//  void QValue3DAxis::setReversed(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QValue3DAxis11setReversedEb(
    QValue3DAxis *self,
    bool enable) {
  self->setReversed(enable);
}

//  bool QValue3DAxis::reversed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QValue3DAxis8reversedEv(const QValue3DAxis *self) {
  return self->reversed();
}

//  void QValue3DAxis::recalculate()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QValue3DAxis11recalculateEv(QValue3DAxis *self) {
  self->recalculate();
}

//  qsizetype QValue3DAxis::gridSize()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN12QValue3DAxis8gridSizeEv(QValue3DAxis *self) {
  return self->gridSize();
}

//  qsizetype QValue3DAxis::subGridSize()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN12QValue3DAxis11subGridSizeEv(QValue3DAxis *self) {
  return self->subGridSize();
}

//  float QValue3DAxis::gridPositionAt(qsizetype gridLine)
extern "C" Q_DECL_EXPORT
float ritual_ZN12QValue3DAxis14gridPositionAtEx(
    QValue3DAxis *self,
    qsizetype gridLine) {
  return self->gridPositionAt(gridLine);
}

//  float QValue3DAxis::subGridPositionAt(qsizetype gridLine)
extern "C" Q_DECL_EXPORT
float ritual_ZN12QValue3DAxis17subGridPositionAtEx(
    QValue3DAxis *self,
    qsizetype gridLine) {
  return self->subGridPositionAt(gridLine);
}

//  float QValue3DAxis::labelPositionAt(qsizetype index)
extern "C" Q_DECL_EXPORT
float ritual_ZN12QValue3DAxis15labelPositionAtEx(
    QValue3DAxis *self,
    qsizetype index) {
  return self->labelPositionAt(index);
}

//  float QValue3DAxis::positionAt(float x)
extern "C" Q_DECL_EXPORT
float ritual_ZN12QValue3DAxis10positionAtEf(QValue3DAxis *self, float x) {
  return self->positionAt(x);
}

//  QString QValue3DAxis::stringForValue(float x)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QValue3DAxis14stringForValueEf(
    QValue3DAxis *self,
    float x) {
  return new QString(self->stringForValue(x));
}

//  void QValue3DAxis::segmentCountChanged(qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QValue3DAxis19segmentCountChangedEx(
    QValue3DAxis *self,
    qsizetype count) {
  self->segmentCountChanged(count);
}

//  void QValue3DAxis::subSegmentCountChanged(qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QValue3DAxis22subSegmentCountChangedEx(
    QValue3DAxis *self,
    qsizetype count) {
  self->subSegmentCountChanged(count);
}

//  void QValue3DAxis::labelFormatChanged(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QValue3DAxis18labelFormatChangedERK7QString(
    QValue3DAxis *self,
    const QString *format) {
  self->labelFormatChanged(*format);
}

//  void QValue3DAxis::formatterChanged(QValue3DAxisFormatter *formatter)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QValue3DAxis16formatterChangedEP21QValue3DAxisFormatter(
    QValue3DAxis *self,
    QValue3DAxisFormatter *formatter) {
  self->formatterChanged(formatter);
}

//  void QValue3DAxis::reversedChanged(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QValue3DAxis15reversedChangedEb(
    QValue3DAxis *self,
    bool enable) {
  self->reversedChanged(enable);
}

//  void QValue3DAxis::formatterDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QValue3DAxis14formatterDirtyEv(QValue3DAxis *self) {
  self->formatterDirty();
}

//  a Python function taken by a CuteQValue3DAxis, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QValue3DAxis(
    QValue3DAxis *self,
    const char *key,
    void *call) {
  return static_cast<CuteQValue3DAxis *>(self)->take(key, call);
}

//  QList<QValue3DAxis *>::QList()
extern "C" Q_DECL_EXPORT
QList<QValue3DAxis *> *ritual_list_make_QValue3DAxis_ptr() {
  return new QList<QValue3DAxis *>();
}

//  void QList<QValue3DAxis *>::append(const QValue3DAxis * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QValue3DAxis_ptr(
    QList<QValue3DAxis *> *self,
    QValue3DAxis *element) {
  self->append(element);
}

//  qsizetype QList<QValue3DAxis *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QValue3DAxis_ptr(
    const QList<QValue3DAxis *> *self) {
  return self->size();
}

//  const QValue3DAxis * &QList<QValue3DAxis *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_list_at_QValue3DAxis_ptr(
    const QList<QValue3DAxis *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QValue3DAxis *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QValue3DAxis_ptr(QList<QValue3DAxis *> *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
