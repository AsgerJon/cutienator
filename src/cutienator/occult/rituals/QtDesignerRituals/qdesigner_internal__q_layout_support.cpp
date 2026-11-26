//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qlayout_widget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qlayout_widget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtWidgets/qwidget.h>
#include <QtCore/qrect.h>
#include <QtGui/qpalette.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <utility>

//  Only a class built on qdesigner_internal::QLayoutSupport may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct Ownqdesigner_internal_QLayoutSupport : qdesigner_internal::QLayoutSupport {
  using qdesigner_internal::QLayoutSupport::itemInfo;
};

//  A qdesigner_internal::QLayoutSupport that Python can take functions over in. Every qdesigner_internal::QLayoutSupport
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*Cuteqdesigner_internal_QLayoutSupportCall0)(const void *, int *);
typedef int (*Cuteqdesigner_internal_QLayoutSupportCall1)(const void *, int *);
typedef int (*Cuteqdesigner_internal_QLayoutSupportCall2)(const void *, const QPoint *, int *);
typedef int (*Cuteqdesigner_internal_QLayoutSupportCall3)(const void *, QWidget *, int *);
typedef int (*Cuteqdesigner_internal_QLayoutSupportCall4)(const void *, QLayoutItem *, int *);
typedef void (*Cuteqdesigner_internal_QLayoutSupportCall5)(const void *, const QPoint *, int, int *);
typedef void (*Cuteqdesigner_internal_QLayoutSupportCall6)(const void *, int, int *);
typedef void (*Cuteqdesigner_internal_QLayoutSupportCall7)(const void *, int, int, int, int *);
typedef const QRect * (*Cuteqdesigner_internal_QLayoutSupportCall8)(const void *, int, int *);
typedef bool (*Cuteqdesigner_internal_QLayoutSupportCall9)(const void *, int, int *);
typedef const QRect * (*Cuteqdesigner_internal_QLayoutSupportCall10)(const void *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_QLayoutSupportCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_QLayoutSupportCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QLayoutSupportCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QLayoutSupportCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QLayoutSupportCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QLayoutSupportCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QLayoutSupportCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QLayoutSupportCall18)(const void *, QWidget *, int *);
typedef void (*Cuteqdesigner_internal_QLayoutSupportCall19)(const void *, int, int *);
typedef void (*Cuteqdesigner_internal_QLayoutSupportCall20)(const void *, int, int *);
typedef void (*Cuteqdesigner_internal_QLayoutSupportCall21)(const void *, int *);
typedef int (*Cuteqdesigner_internal_QLayoutSupportCall22)(const void *, int, int, int *);
class Cuteqdesigner_internal_QLayoutSupport : public qdesigner_internal::QLayoutSupport {
public:
  using qdesigner_internal::QLayoutSupport::QLayoutSupport;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK34QDesignerLayoutDecorationExtension12currentIndexEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerLayoutDecorationExtension17currentInsertModeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerLayoutDecorationExtension10findItemAtERK6QPoint")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerLayoutDecorationExtension7indexOfEP7QWidget")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerLayoutDecorationExtension7indexOfEP11QLayoutItem")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDesignerLayoutDecorationExtension15adjustIndicatorERK6QPointi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal14QLayoutSupport38setCurrentCellFromIndicatorOnEmptyCellEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal14QLayoutSupport27setCurrentCellFromIndicatorEN2Qt11OrientationEii")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18qdesigner_internal14QLayoutSupport16extendedGeometryEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18qdesigner_internal14QLayoutSupport28supportsIndicatorOrientationEN2Qt11OrientationE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerLayoutDecorationExtension8itemInfoEi")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN34QDesignerLayoutDecorationExtension12removeWidgetEP7QWidget")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDesignerLayoutDecorationExtension9insertRowEi")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDesignerLayoutDecorationExtension12insertColumnEi")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDesignerLayoutDecorationExtension8simplifyEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerLayoutDecorationExtension10findItemAtEii")) {
      taken[22] = call;
      return true;
    }
    return false;
  }

  //  int qdesigner_internal::QLayoutSupport::currentIndex() const
  int currentIndex() const override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall0 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return qdesigner_internal::QLayoutSupport::currentIndex();
  }

  //  InsertMode qdesigner_internal::QLayoutSupport::currentInsertMode()
  //      const
  QDesignerLayoutDecorationExtension::InsertMode currentInsertMode() const override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall1 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDesignerLayoutDecorationExtension::InsertMode>(given);
    }
    return qdesigner_internal::QLayoutSupport::currentInsertMode();
  }

  //  int qdesigner_internal::QLayoutSupport::findItemAt(const QPoint &pos)
  //      const
  int findItemAt(const QPoint &pos) const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall2 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall2>(taken[2]);
      int given = call(this, &pos, &handled);
      if (handled) return given;
    }
    return qdesigner_internal::QLayoutSupport::findItemAt(pos);
  }

  //  int qdesigner_internal::QLayoutSupport::indexOf(QWidget *widget)
  //      const
  int indexOf(QWidget *widget) const override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall3 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall3>(taken[3]);
      int given = call(this, widget, &handled);
      if (handled) return given;
    }
    return qdesigner_internal::QLayoutSupport::indexOf(widget);
  }

  //  int qdesigner_internal::QLayoutSupport::indexOf(QLayoutItem *item)
  //      const
  int indexOf(QLayoutItem *item) const override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall4 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall4>(taken[4]);
      int given = call(this, item, &handled);
      if (handled) return given;
    }
    return qdesigner_internal::QLayoutSupport::indexOf(item);
  }

  //  void qdesigner_internal::QLayoutSupport::adjustIndicator(const QPoint
  //      &pos, int index)
  void adjustIndicator(const QPoint &pos, int index) override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall5 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall5>(taken[5]);
      call(this, &pos, index, &handled);
      if (handled) return;
    }
    qdesigner_internal::QLayoutSupport::adjustIndicator(pos, index);
  }

  //  void qdesigner_internal::QLayoutSupport::setCurrentCellFromIndicatorO
  //      nEmptyCell(int index)
  void setCurrentCellFromIndicatorOnEmptyCell(int index) override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall6 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall6>(taken[6]);
      call(this, index, &handled);
      if (handled) return;
    }
  }

  //  void qdesigner_internal::QLayoutSupport::setCurrentCellFromIndicator(
  //      Qt::Orientation indicatorOrientation, int index, int increment)
  void setCurrentCellFromIndicator(
      Qt::Orientation indicatorOrientation,
      int index,
      int increment) override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall7 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall7>(taken[7]);
      call(this, static_cast<int>(indicatorOrientation), index, increment, &handled);
      if (handled) return;
    }
  }

  //  QRect qdesigner_internal::QLayoutSupport::extendedGeometry(int index)
  //      const
  QRect extendedGeometry(int index) const override {
    if (taken[8]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall8 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall8>(taken[8]);
      const QRect * given = call(this, index, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool qdesigner_internal::QLayoutSupport::supportsIndicatorOrientation
  //      (Qt::Orientation indicatorOrientation) const
  bool supportsIndicatorOrientation(
      Qt::Orientation indicatorOrientation) const override {
    if (taken[9]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall9 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall9>(taken[9]);
      bool given = call(this, static_cast<int>(indicatorOrientation), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QRect qdesigner_internal::QLayoutSupport::itemInfo(int index) const
  QRect itemInfo(int index) const override {
    if (taken[10]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall10 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall10>(taken[10]);
      const QRect * given = call(this, index, &handled);
      if (handled && given) return *given;
    }
    return qdesigner_internal::QLayoutSupport::itemInfo(index);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall11 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall11>(taken[11]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall12 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall12>(taken[12]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall13 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall14 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall15 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall16 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall17 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QDesignerLayoutDecorationExtension::removeWidget(QWidget
  //      *widget)
  void removeWidget(QWidget *widget) override {
    if (taken[18]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall18 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall18>(taken[18]);
      call(this, widget, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerLayoutDecorationExtension::insertRow(int row)
  void insertRow(int row) override {
    if (taken[19]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall19 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall19>(taken[19]);
      call(this, row, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerLayoutDecorationExtension::insertColumn(int column)
  void insertColumn(int column) override {
    if (taken[20]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall20 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall20>(taken[20]);
      call(this, column, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerLayoutDecorationExtension::simplify()
  void simplify() override {
    if (taken[21]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall21 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  int QDesignerLayoutDecorationExtension::findItemAt(int row, int
  //      column) const
  int findItemAt(int row, int column) const override {
    if (taken[22]) {
      int handled = 0;
      Cuteqdesigner_internal_QLayoutSupportCall22 call = reinterpret_cast<Cuteqdesigner_internal_QLayoutSupportCall22>(taken[22]);
      int given = call(this, row, column, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  const QMetaObject *qdesigner_internal::QLayoutSupport::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal14QLayoutSupport10metaObjectEv(
    const qdesigner_internal::QLayoutSupport *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::QLayoutSupport::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal14QLayoutSupport11qt_metacastEPKc(
    qdesigner_internal::QLayoutSupport *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::QLayoutSupport::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal14QLayoutSupport11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::QLayoutSupport *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::QLayoutSupport::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal14QLayoutSupport2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::QLayoutSupport::tr(s, c, n));
}

//  qdesigner_internal::QLayoutSupport::~QLayoutSupport()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14QLayoutSupportD1Ev(
    qdesigner_internal::QLayoutSupport *self) {
  delete self;
}

//  QDesignerFormWindowInterface
//      *qdesigner_internal::QLayoutSupport::formWindow() const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface *ritual_ZNK18qdesigner_internal14QLayoutSupport10formWindowEv(
    const qdesigner_internal::QLayoutSupport *self) {
  return self->formWindow();
}

//  LayoutHelper *qdesigner_internal::QLayoutSupport::helper() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::LayoutHelper *ritual_ZNK18qdesigner_internal14QLayoutSupport6helperEv(
    const qdesigner_internal::QLayoutSupport *self) {
  return self->helper();
}

//  int qdesigner_internal::QLayoutSupport::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal14QLayoutSupport12currentIndexEv(
    const qdesigner_internal::QLayoutSupport *self) {
  return self->currentIndex();
}

//  InsertMode qdesigner_internal::QLayoutSupport::currentInsertMode() const
extern "C" Q_DECL_EXPORT
QDesignerLayoutDecorationExtension::InsertMode ritual_ZNK18qdesigner_internal14QLayoutSupport17currentInsertModeEv(
    const qdesigner_internal::QLayoutSupport *self) {
  return self->currentInsertMode();
}

//  std::pair<int, int> qdesigner_internal::QLayoutSupport::currentCell()
//      const
extern "C" Q_DECL_EXPORT
std::pair<int, int> *ritual_ZNK18qdesigner_internal14QLayoutSupport11currentCellEv(
    const qdesigner_internal::QLayoutSupport *self) {
  return new std::pair<int, int>(self->currentCell());
}

//  int qdesigner_internal::QLayoutSupport::findItemAt(const QPoint &pos)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal14QLayoutSupport10findItemAtERK6QPoint(
    const qdesigner_internal::QLayoutSupport *self,
    const QPoint *pos) {
  return self->findItemAt(*pos);
}

//  int qdesigner_internal::QLayoutSupport::indexOf(QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal14QLayoutSupport7indexOfEP7QWidget(
    const qdesigner_internal::QLayoutSupport *self,
    QWidget *widget) {
  return self->indexOf(widget);
}

//  int qdesigner_internal::QLayoutSupport::indexOf(QLayoutItem *item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal14QLayoutSupport7indexOfEP11QLayoutItem(
    const qdesigner_internal::QLayoutSupport *self,
    QLayoutItem *item) {
  return self->indexOf(item);
}

//  void qdesigner_internal::QLayoutSupport::adjustIndicator(const QPoint
//      &pos, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14QLayoutSupport15adjustIndicatorERK6QPointi(
    qdesigner_internal::QLayoutSupport *self,
    const QPoint *pos,
    int index) {
  self->adjustIndicator(*pos, index);
}

//  QWidgetList qdesigner_internal::QLayoutSupport::widgets(QLayout *layout)
//      const
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZNK18qdesigner_internal14QLayoutSupport7widgetsEP7QLayout(
    const qdesigner_internal::QLayoutSupport *self,
    QLayout *layout) {
  return new QList<QWidget *>(self->widgets(layout));
}

//  void qdesigner_internal::QLayoutSupport::createEmptyCells(QGridLayout
//      *gridLayout)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14QLayoutSupport16createEmptyCellsEP11QGridLayout(
    QGridLayout *gridLayout) {
  qdesigner_internal::QLayoutSupport::createEmptyCells(gridLayout);
}

//  bool qdesigner_internal::QLayoutSupport::removeEmptyCells(QGridLayout
//      *gridLayout, const QRect &area)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal14QLayoutSupport16removeEmptyCellsEP11QGridLayoutRK5QRect(
    QGridLayout *gridLayout,
    const QRect *area) {
  return qdesigner_internal::QLayoutSupport::removeEmptyCells(
      gridLayout,
      *area);
}

//  void qdesigner_internal::QLayoutSupport::createEmptyCells(QFormLayout
//      *formLayout)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14QLayoutSupport16createEmptyCellsEP11QFormLayout(
    QFormLayout *formLayout) {
  qdesigner_internal::QLayoutSupport::createEmptyCells(formLayout);
}

//  bool qdesigner_internal::QLayoutSupport::removeEmptyCells(QFormLayout
//      *formLayout, const QRect &area)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal14QLayoutSupport16removeEmptyCellsEP11QFormLayoutRK5QRect(
    QFormLayout *formLayout,
    const QRect *area) {
  return qdesigner_internal::QLayoutSupport::removeEmptyCells(
      formLayout,
      *area);
}

//  int qdesigner_internal::QLayoutSupport::findItemAt(QGridLayout *a0, int
//      row, int column)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal14QLayoutSupport10findItemAtEP11QGridLayoutii(
    QGridLayout *a0,
    int row,
    int column) {
  return qdesigner_internal::QLayoutSupport::findItemAt(a0, row, column);
}

//  bool qdesigner_internal::QLayoutSupport::canSimplifyQuickCheck(const
//      QGridLayout *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal14QLayoutSupport21canSimplifyQuickCheckEPK11QGridLayout(
    const QGridLayout *a0) {
  return qdesigner_internal::QLayoutSupport::canSimplifyQuickCheck(a0);
}

//  bool qdesigner_internal::QLayoutSupport::canSimplifyQuickCheck(const
//      QFormLayout *fl)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal14QLayoutSupport21canSimplifyQuickCheckEPK11QFormLayout(
    const QFormLayout *fl) {
  return qdesigner_internal::QLayoutSupport::canSimplifyQuickCheck(fl);
}

//  QLayoutSupport *qdesigner_internal::QLayoutSupport::createLayoutSupport(Q
//      DesignerFormWindowInterface *formWindow, QWidget *widget, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::QLayoutSupport *ritual_ZN18qdesigner_internal14QLayoutSupport19createLayoutSupportEP28QDesignerFormWindowInterfaceP7QWidgetP7QObject(
    QDesignerFormWindowInterface *formWindow,
    QWidget *widget,
    QObject *parent) {
  return qdesigner_internal::QLayoutSupport::createLayoutSupport(
      formWindow,
      widget,
      parent);
}

//  void qdesigner_internal::QLayoutSupport::setCurrentCellFromIndicatorOnEmp
//      tyCell(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14QLayoutSupport38setCurrentCellFromIndicatorOnEmptyCellEi(
    qdesigner_internal::QLayoutSupport *self,
    int index) {
  self->setCurrentCellFromIndicatorOnEmptyCell(index);
}

//  void qdesigner_internal::QLayoutSupport::setCurrentCellFromIndicator(Qt::
//      Orientation indicatorOrientation, int index, int increment)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14QLayoutSupport27setCurrentCellFromIndicatorEN2Qt11OrientationEii(
    qdesigner_internal::QLayoutSupport *self,
    Qt::Orientation indicatorOrientation,
    int index,
    int increment) {
  self->setCurrentCellFromIndicator(indicatorOrientation, index, increment);
}

//  QRect qdesigner_internal::QLayoutSupport::extendedGeometry(int index)
//      const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18qdesigner_internal14QLayoutSupport16extendedGeometryEi(
    const qdesigner_internal::QLayoutSupport *self,
    int index) {
  return new QRect(self->extendedGeometry(index));
}

//  bool qdesigner_internal::QLayoutSupport::supportsIndicatorOrientation(Qt:
//      :Orientation indicatorOrientation) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal14QLayoutSupport28supportsIndicatorOrientationEN2Qt11OrientationE(
    const qdesigner_internal::QLayoutSupport *self,
    Qt::Orientation indicatorOrientation) {
  return self->supportsIndicatorOrientation(indicatorOrientation);
}

//  QRect qdesigner_internal::QLayoutSupport::itemInfo(int index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18qdesigner_internal14QLayoutSupport8itemInfoEi(
    const qdesigner_internal::QLayoutSupport *self,
    int index) {
  return new QRect(self->itemInfo(index));
}

//  QLayout *qdesigner_internal::QLayoutSupport::layout() const
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZNK18qdesigner_internal14QLayoutSupport6layoutEv(
    const qdesigner_internal::QLayoutSupport *self) {
  return self->layout();
}

//  QGridLayout *qdesigner_internal::QLayoutSupport::gridLayout() const
extern "C" Q_DECL_EXPORT
QGridLayout *ritual_ZNK18qdesigner_internal14QLayoutSupport10gridLayoutEv(
    const qdesigner_internal::QLayoutSupport *self) {
  return self->gridLayout();
}

//  QWidget *qdesigner_internal::QLayoutSupport::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK18qdesigner_internal14QLayoutSupport6widgetEv(
    const qdesigner_internal::QLayoutSupport *self) {
  return self->widget();
}

//  void qdesigner_internal::QLayoutSupport::setInsertMode(InsertMode im)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14QLayoutSupport13setInsertModeEN34QDesignerLayoutDecorationExtension10InsertModeE(
    qdesigner_internal::QLayoutSupport *self,
    QDesignerLayoutDecorationExtension::InsertMode im) {
  self->setInsertMode(im);
}

//  void qdesigner_internal::QLayoutSupport::setCurrentCell(const
//      std::pair<int, int> &cell)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14QLayoutSupport14setCurrentCellERKSt4pairIiiE(
    qdesigner_internal::QLayoutSupport *self,
    const std::pair<int, int> *cell) {
  self->setCurrentCell(*cell);
}

//  void qdesigner_internal::QLayoutSupport::hideIndicator(Indicator i)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14QLayoutSupport13hideIndicatorENS0_9IndicatorE(
    qdesigner_internal::QLayoutSupport *self,
    qdesigner_internal::QLayoutSupport::Indicator i) {
  self->hideIndicator(i);
}

//  void qdesigner_internal::QLayoutSupport::showIndicator(Indicator i, const
//      QRect &geometry, const QPalette &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14QLayoutSupport13showIndicatorENS0_9IndicatorERK5QRectRK8QPalette(
    qdesigner_internal::QLayoutSupport *self,
    qdesigner_internal::QLayoutSupport::Indicator i,
    const QRect *geometry,
    const QPalette *a2) {
  self->showIndicator(i, *geometry, *a2);
}

//  qdesigner_internal::QLayoutSupport as the
//      QDesignerLayoutDecorationExtension it is built on
extern "C" Q_DECL_EXPORT
QDesignerLayoutDecorationExtension *ritual_cast_qdesigner_internal_QLayoutSupport_QDesignerLayoutDecorationExtension(
    qdesigner_internal::QLayoutSupport *self) {
  return static_cast<QDesignerLayoutDecorationExtension *>(self);
}

//  a Python function taken by a Cuteqdesigner_internal_QLayoutSupport, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_QLayoutSupport(
    qdesigner_internal::QLayoutSupport *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_QLayoutSupport *>(self)->take(key, call);
}

//  int qdesigner_internal::QLayoutSupport::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18qdesigner_internal14QLayoutSupport12currentIndexEv(
    const qdesigner_internal::QLayoutSupport *self) {
  return self->qdesigner_internal::QLayoutSupport::currentIndex();
}

//  InsertMode qdesigner_internal::QLayoutSupport::currentInsertMode() const
extern "C" Q_DECL_EXPORT
QDesignerLayoutDecorationExtension::InsertMode ritual_own_ZNK18qdesigner_internal14QLayoutSupport17currentInsertModeEv(
    const qdesigner_internal::QLayoutSupport *self) {
  return self->qdesigner_internal::QLayoutSupport::currentInsertMode();
}

//  int qdesigner_internal::QLayoutSupport::findItemAt(const QPoint &pos)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18qdesigner_internal14QLayoutSupport10findItemAtERK6QPoint(
    const qdesigner_internal::QLayoutSupport *self,
    const QPoint *pos) {
  return self->qdesigner_internal::QLayoutSupport::findItemAt(*pos);
}

//  int qdesigner_internal::QLayoutSupport::indexOf(QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18qdesigner_internal14QLayoutSupport7indexOfEP7QWidget(
    const qdesigner_internal::QLayoutSupport *self,
    QWidget *widget) {
  return self->qdesigner_internal::QLayoutSupport::indexOf(widget);
}

//  int qdesigner_internal::QLayoutSupport::indexOf(QLayoutItem *item) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18qdesigner_internal14QLayoutSupport7indexOfEP11QLayoutItem(
    const qdesigner_internal::QLayoutSupport *self,
    QLayoutItem *item) {
  return self->qdesigner_internal::QLayoutSupport::indexOf(item);
}

//  void qdesigner_internal::QLayoutSupport::adjustIndicator(const QPoint
//      &pos, int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14QLayoutSupport15adjustIndicatorERK6QPointi(
    qdesigner_internal::QLayoutSupport *self,
    const QPoint *pos,
    int index) {
  self->qdesigner_internal::QLayoutSupport::adjustIndicator(*pos, index);
}

//  QRect qdesigner_internal::QLayoutSupport::itemInfo(int index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK18qdesigner_internal14QLayoutSupport8itemInfoEi(
    const qdesigner_internal::QLayoutSupport *self,
    int index) {
  return new QRect(
      static_cast<const Ownqdesigner_internal_QLayoutSupport *>(self)->Ownqdesigner_internal_QLayoutSupport::itemInfo(
          index));
}

//  a std::pair<int, int> a ritual of qdesigner_internal::QLayoutSupport gave
extern "C" Q_DECL_EXPORT
void ritual_drop_qdesigner_internal_QLayoutSupport__std_pair_int_int(
    std::pair<int, int> *self) {
  delete self;
}
