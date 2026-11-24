//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qbarset.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_bar))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qbarset.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QBarSet that Python can take functions over in. Every QBarSet
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarSetCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarSetCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarSetCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarSetCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarSetCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarSetCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarSetCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBarSet : public QBarSet {
public:
  using QBarSet::QBarSet;
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
      CuteQBarSetCall0 call = reinterpret_cast<CuteQBarSetCall0>(taken[0]);
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
      CuteQBarSetCall1 call = reinterpret_cast<CuteQBarSetCall1>(taken[1]);
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
      CuteQBarSetCall2 call = reinterpret_cast<CuteQBarSetCall2>(taken[2]);
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
      CuteQBarSetCall3 call = reinterpret_cast<CuteQBarSetCall3>(taken[3]);
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
      CuteQBarSetCall4 call = reinterpret_cast<CuteQBarSetCall4>(taken[4]);
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
      CuteQBarSetCall5 call = reinterpret_cast<CuteQBarSetCall5>(taken[5]);
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
      CuteQBarSetCall6 call = reinterpret_cast<CuteQBarSetCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBarSet::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QBarSet10metaObjectEv(const QBarSet *self) {
  return self->metaObject();
}

//  QString QBarSet::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QBarSet2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QBarSet::tr(s, c, n));
}

//  QBarSetPrivate *QBarSet::d_func()
extern "C" Q_DECL_EXPORT
QBarSetPrivate *ritual_ZN7QBarSet6d_funcEv(QBarSet *self) {
  return self->d_func();
}

//  const QBarSetPrivate *QBarSet::d_func() const
extern "C" Q_DECL_EXPORT
const QBarSetPrivate *ritual_ZNK7QBarSet6d_funcEv(const QBarSet *self) {
  return self->d_func();
}

//  QBarSet::QBarSet(QObject *parent)
extern "C" Q_DECL_EXPORT
QBarSet *ritual_ZN7QBarSetC1EP7QObject(QObject *parent) {
  return new CuteQBarSet(parent);
}

//  QBarSet::QBarSet(const QString &label, QObject *parent)
extern "C" Q_DECL_EXPORT
QBarSet *ritual_ZN7QBarSetC1ERK7QStringP7QObject(
    const QString *label,
    QObject *parent) {
  return new CuteQBarSet(*label, parent);
}

//  QBarSet::~QBarSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBarSetD1Ev(QBarSet *self) {
  delete self;
}

//  void QBarSet::setLabel(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBarSet8setLabelERK7QString(
    QBarSet *self,
    const QString *label) {
  self->setLabel(*label);
}

//  QString QBarSet::label() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QBarSet5labelEv(const QBarSet *self) {
  return new QString(self->label());
}

//  void QBarSet::append(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBarSet6appendEd(QBarSet *self, qreal value) {
  self->append(value);
}

//  void QBarSet::insert(qsizetype index, qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBarSet6insertExd(
    QBarSet *self,
    qsizetype index,
    qreal value) {
  self->insert(index, value);
}

//  void QBarSet::remove(qsizetype index, qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBarSet6removeExx(
    QBarSet *self,
    qsizetype index,
    qsizetype count) {
  self->remove(index, count);
}

//  void QBarSet::replace(qsizetype index, qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBarSet7replaceExd(
    QBarSet *self,
    qsizetype index,
    qreal value) {
  self->replace(index, value);
}

//  qreal QBarSet::at(qsizetype index) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QBarSet2atEx(const QBarSet *self, qsizetype index) {
  return self->at(index);
}

//  qsizetype QBarSet::count() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QBarSet5countEv(const QBarSet *self) {
  return self->count();
}

//  qreal QBarSet::sum() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QBarSet3sumEv(const QBarSet *self) {
  return self->sum();
}

//  void QBarSet::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBarSet5clearEv(QBarSet *self) {
  self->clear();
}

//  qreal QBarSet::operator[](qsizetype index) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QBarSetixEx(const QBarSet *self, qsizetype index) {
  return self->operator[](index);
}

//  QColor QBarSet::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK7QBarSet5colorEv(const QBarSet *self) {
  return new QColor(self->color());
}

//  void QBarSet::setColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBarSet8setColorE6QColor(QBarSet *self, const QColor *color) {
  self->setColor(*color);
}

//  QColor QBarSet::borderColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK7QBarSet11borderColorEv(const QBarSet *self) {
  return new QColor(self->borderColor());
}

//  void QBarSet::setBorderColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBarSet14setBorderColorE6QColor(
    QBarSet *self,
    const QColor *color) {
  self->setBorderColor(*color);
}

//  QColor QBarSet::labelColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK7QBarSet10labelColorEv(const QBarSet *self) {
  return new QColor(self->labelColor());
}

//  void QBarSet::setLabelColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBarSet13setLabelColorE6QColor(
    QBarSet *self,
    const QColor *color) {
  self->setLabelColor(*color);
}

//  QColor QBarSet::selectedColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK7QBarSet13selectedColorEv(const QBarSet *self) {
  return new QColor(self->selectedColor());
}

//  void QBarSet::setSelectedColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBarSet16setSelectedColorE6QColor(
    QBarSet *self,
    const QColor *color) {
  self->setSelectedColor(*color);
}

//  QVariantList QBarSet::values() const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK7QBarSet6valuesEv(const QBarSet *self) {
  return new QList<QVariant>(self->values());
}

//  void QBarSet::setValues(const QVariantList &values)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBarSet9setValuesERK5QListI8QVariantE(
    QBarSet *self,
    const QList<QVariant> *values) {
  self->setValues(*values);
}

//  qreal QBarSet::borderWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QBarSet11borderWidthEv(const QBarSet *self) {
  return self->borderWidth();
}

//  void QBarSet::setBorderWidth(qreal borderWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBarSet14setBorderWidthEd(QBarSet *self, qreal borderWidth) {
  self->setBorderWidth(borderWidth);
}

//  bool QBarSet::isBarSelected(qsizetype index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QBarSet13isBarSelectedEx(
    const QBarSet *self,
    qsizetype index) {
  return self->isBarSelected(index);
}

//  void QBarSet::selectBar(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBarSet9selectBarEx(QBarSet *self, qsizetype index) {
  self->selectBar(index);
}

//  void QBarSet::deselectBar(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBarSet11deselectBarEx(QBarSet *self, qsizetype index) {
  self->deselectBar(index);
}

//  void QBarSet::setBarSelected(qsizetype index, bool selected)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBarSet14setBarSelectedExb(
    QBarSet *self,
    qsizetype index,
    bool selected) {
  self->setBarSelected(index, selected);
}

//  void QBarSet::selectAllBars()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBarSet13selectAllBarsEv(QBarSet *self) {
  self->selectAllBars();
}

//  void QBarSet::deselectAllBars()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBarSet15deselectAllBarsEv(QBarSet *self) {
  self->deselectAllBars();
}

//  a Python function taken by a CuteQBarSet, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBarSet(QBarSet *self, const char *key, void *call) {
  return static_cast<CuteQBarSet *>(self)->take(key, call);
}

//  QList<QBarSet *>::QList()
extern "C" Q_DECL_EXPORT
QList<QBarSet *> *ritual_list_make_QBarSet_ptr() {
  return new QList<QBarSet *>();
}

//  void QList<QBarSet *>::append(const QBarSet * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QBarSet_ptr(QList<QBarSet *> *self, QBarSet *element) {
  self->append(element);
}

//  qsizetype QList<QBarSet *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QBarSet_ptr(const QList<QBarSet *> *self) {
  return self->size();
}

//  const QBarSet * &QList<QBarSet *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QBarSet *ritual_list_at_QBarSet_ptr(
    const QList<QBarSet *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QBarSet *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QBarSet_ptr(QList<QBarSet *> *self) {
  delete self;
}

#endif  // (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_bar))
