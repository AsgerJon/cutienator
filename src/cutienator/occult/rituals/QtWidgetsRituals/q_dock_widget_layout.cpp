//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qdockwidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qdockwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDockWidgetLayout that Python can take functions over in. Every QDockWidgetLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(dockwidget)
typedef void (*CuteQDockWidgetLayoutCall0)(const void *, QLayoutItem *, int *);
#endif  // QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
typedef void * (*CuteQDockWidgetLayoutCall1)(const void *, int, int *);
#endif  // QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
typedef void * (*CuteQDockWidgetLayoutCall2)(const void *, int, int *);
#endif  // QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
typedef int (*CuteQDockWidgetLayoutCall3)(const void *, int *);
#endif  // QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
typedef const QSize * (*CuteQDockWidgetLayoutCall4)(const void *, int *);
#endif  // QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
typedef const QSize * (*CuteQDockWidgetLayoutCall5)(const void *, int *);
#endif  // QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
typedef const QSize * (*CuteQDockWidgetLayoutCall6)(const void *, int *);
#endif  // QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
typedef void (*CuteQDockWidgetLayoutCall7)(const void *, const QRect *, int *);
#endif  // QT_CONFIG(dockwidget)
typedef int (*CuteQDockWidgetLayoutCall8)(const void *, int *);
typedef void (*CuteQDockWidgetLayoutCall9)(const void *, int, int *);
typedef void (*CuteQDockWidgetLayoutCall10)(const void *, int *);
typedef const QRect * (*CuteQDockWidgetLayoutCall11)(const void *, int *);
typedef int (*CuteQDockWidgetLayoutCall12)(const void *, int *);
typedef int (*CuteQDockWidgetLayoutCall13)(const void *, const QWidget *, int *);
typedef int (*CuteQDockWidgetLayoutCall14)(const void *, const QLayoutItem *, int *);
typedef bool (*CuteQDockWidgetLayoutCall15)(const void *, int *);
typedef int (*CuteQDockWidgetLayoutCall16)(const void *, int *);
typedef void * (*CuteQDockWidgetLayoutCall17)(const void *, QWidget *, QWidget *, int, int *);
typedef void * (*CuteQDockWidgetLayoutCall18)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDockWidgetLayoutCall19)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDockWidgetLayoutCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDockWidgetLayoutCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDockWidgetLayoutCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDockWidgetLayoutCall23)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDockWidgetLayoutCall24)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDockWidgetLayoutCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDockWidgetLayoutCall26)(const void *, int *);
typedef int (*CuteQDockWidgetLayoutCall27)(const void *, int, int *);
typedef int (*CuteQDockWidgetLayoutCall28)(const void *, int, int *);
typedef void * (*CuteQDockWidgetLayoutCall29)(const void *, int *);
typedef void * (*CuteQDockWidgetLayoutCall30)(const void *, int *);
class CuteQDockWidgetLayout : public QDockWidgetLayout {
public:
  using QDockWidgetLayout::QDockWidgetLayout;
  void *taken[31] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZN7QLayout7addItemEP11QLayoutItem")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZNK7QLayout6itemAtEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZN7QLayout6takeAtEi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZNK7QLayout5countEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZNK11QLayoutItem11maximumSizeEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZNK11QLayoutItem11minimumSizeEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZNK11QLayoutItem8sizeHintEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZN11QLayoutItem11setGeometryERK5QRect")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZNK7QLayout7spacingEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout10setSpacingEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem10invalidateEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem8geometryEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem19expandingDirectionsEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7indexOfEPK7QWidget")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7indexOfEPK11QLayoutItem")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem7isEmptyEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem12controlTypesEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout13replaceWidgetEP7QWidgetS1_6QFlagsIN2Qt15FindChildOptionEE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem6layoutEv")) {
      taken[18] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK11QLayoutItem17hasHeightForWidthEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem14heightForWidthEi")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem21minimumHeightForWidthEi")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem6widgetEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem10spacerItemEv")) {
      taken[30] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(dockwidget)
  //  void QDockWidgetLayout::addItem(QLayoutItem *item)
  void addItem(QLayoutItem *item) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall0 call = reinterpret_cast<CuteQDockWidgetLayoutCall0>(taken[0]);
      call(this, item, &handled);
      if (handled) return;
    }
    QDockWidgetLayout::addItem(item);
  }
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(dockwidget)
  //  QLayoutItem *QDockWidgetLayout::itemAt(int index) const
  QLayoutItem *itemAt(int index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall1 call = reinterpret_cast<CuteQDockWidgetLayoutCall1>(taken[1]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QDockWidgetLayout::itemAt(index);
  }
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(dockwidget)
  //  QLayoutItem *QDockWidgetLayout::takeAt(int index)
  QLayoutItem *takeAt(int index) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall2 call = reinterpret_cast<CuteQDockWidgetLayoutCall2>(taken[2]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QDockWidgetLayout::takeAt(index);
  }
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(dockwidget)
  //  int QDockWidgetLayout::count() const
  int count() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall3 call = reinterpret_cast<CuteQDockWidgetLayoutCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDockWidgetLayout::count();
  }
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(dockwidget)
  //  QSize QDockWidgetLayout::maximumSize() const
  QSize maximumSize() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall4 call = reinterpret_cast<CuteQDockWidgetLayoutCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDockWidgetLayout::maximumSize();
  }
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(dockwidget)
  //  QSize QDockWidgetLayout::minimumSize() const
  QSize minimumSize() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall5 call = reinterpret_cast<CuteQDockWidgetLayoutCall5>(taken[5]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDockWidgetLayout::minimumSize();
  }
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(dockwidget)
  //  QSize QDockWidgetLayout::sizeHint() const
  QSize sizeHint() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall6 call = reinterpret_cast<CuteQDockWidgetLayoutCall6>(taken[6]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDockWidgetLayout::sizeHint();
  }
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(dockwidget)
  //  void QDockWidgetLayout::setGeometry(const QRect &r)
  void setGeometry(const QRect &r) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall7 call = reinterpret_cast<CuteQDockWidgetLayoutCall7>(taken[7]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QDockWidgetLayout::setGeometry(r);
  }
#endif  // QT_CONFIG(dockwidget)

  //  int QLayout::spacing() const
  int spacing() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall8 call = reinterpret_cast<CuteQDockWidgetLayoutCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QLayout::spacing();
  }

  //  void QLayout::setSpacing(int a0)
  void setSpacing(int a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall9 call = reinterpret_cast<CuteQDockWidgetLayoutCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLayout::setSpacing(a0);
  }

  //  void QLayout::invalidate()
  void invalidate() override {
    if (taken[10]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall10 call = reinterpret_cast<CuteQDockWidgetLayoutCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QLayout::invalidate();
  }

  //  QRect QLayout::geometry() const
  QRect geometry() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall11 call = reinterpret_cast<CuteQDockWidgetLayoutCall11>(taken[11]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLayout::geometry();
  }

  //  Qt::Orientations QLayout::expandingDirections() const
  Qt::Orientations expandingDirections() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall12 call = reinterpret_cast<CuteQDockWidgetLayoutCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::Orientation>::fromInt(given);
    }
    return QLayout::expandingDirections();
  }

  //  int QLayout::indexOf(const QWidget *a0) const
  int indexOf(const QWidget *a0) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall13 call = reinterpret_cast<CuteQDockWidgetLayoutCall13>(taken[13]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  int QLayout::indexOf(const QLayoutItem *a0) const
  int indexOf(const QLayoutItem *a0) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall14 call = reinterpret_cast<CuteQDockWidgetLayoutCall14>(taken[14]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  bool QLayout::isEmpty() const
  bool isEmpty() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall15 call = reinterpret_cast<CuteQDockWidgetLayoutCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLayout::isEmpty();
  }

  //  QSizePolicy::ControlTypes QLayout::controlTypes() const
  QSizePolicy::ControlTypes controlTypes() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall16 call = reinterpret_cast<CuteQDockWidgetLayoutCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSizePolicy::ControlType>::fromInt(given);
    }
    return QLayout::controlTypes();
  }

  //  QLayoutItem *QLayout::replaceWidget(QWidget *from, QWidget *to,
  //      Qt::FindChildOptions options)
  QLayoutItem *replaceWidget(
      QWidget *from,
      QWidget *to,
      Qt::FindChildOptions options) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall17 call = reinterpret_cast<CuteQDockWidgetLayoutCall17>(taken[17]);
      void * given = call(this, from, to, static_cast<int>(options.toInt()), &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QLayout::replaceWidget(from, to, options);
  }

  //  QLayout *QLayout::layout()
  QLayout *layout() override {
    if (taken[18]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall18 call = reinterpret_cast<CuteQDockWidgetLayoutCall18>(taken[18]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QLayout::layout();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QLayout::childEvent(QChildEvent *e)
  void childEvent(QChildEvent *e) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall19 call = reinterpret_cast<CuteQDockWidgetLayoutCall19>(taken[19]);
      call(this, e, &handled);
      if (handled) return;
    }
    QLayout::childEvent(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall20 call = reinterpret_cast<CuteQDockWidgetLayoutCall20>(taken[20]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall21 call = reinterpret_cast<CuteQDockWidgetLayoutCall21>(taken[21]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall22 call = reinterpret_cast<CuteQDockWidgetLayoutCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall23 call = reinterpret_cast<CuteQDockWidgetLayoutCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall24 call = reinterpret_cast<CuteQDockWidgetLayoutCall24>(taken[24]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall25 call = reinterpret_cast<CuteQDockWidgetLayoutCall25>(taken[25]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  bool QLayoutItem::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall26 call = reinterpret_cast<CuteQDockWidgetLayoutCall26>(taken[26]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLayoutItem::hasHeightForWidth();
  }

  //  int QLayoutItem::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall27 call = reinterpret_cast<CuteQDockWidgetLayoutCall27>(taken[27]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayoutItem::heightForWidth(a0);
  }

  //  int QLayoutItem::minimumHeightForWidth(int a0) const
  int minimumHeightForWidth(int a0) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall28 call = reinterpret_cast<CuteQDockWidgetLayoutCall28>(taken[28]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayoutItem::minimumHeightForWidth(a0);
  }

  //  QWidget *QLayoutItem::widget() const
  QWidget *widget() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall29 call = reinterpret_cast<CuteQDockWidgetLayoutCall29>(taken[29]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QLayoutItem::widget();
  }

  //  QSpacerItem *QLayoutItem::spacerItem()
  QSpacerItem *spacerItem() override {
    if (taken[30]) {
      int handled = 0;
      CuteQDockWidgetLayoutCall30 call = reinterpret_cast<CuteQDockWidgetLayoutCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSpacerItem *>(given);
    }
    return QLayoutItem::spacerItem();
  }
};

//  const QMetaObject *QDockWidgetLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QDockWidgetLayout10metaObjectEv(
    const QDockWidgetLayout *self) {
  return self->metaObject();
}

//  QString QDockWidgetLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QDockWidgetLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDockWidgetLayout::tr(s, c, n));
}

//  QDockWidgetLayout::QDockWidgetLayout(QWidget *parent)
extern "C" Q_DECL_EXPORT
QDockWidgetLayout *ritual_ZN17QDockWidgetLayoutC1EP7QWidget(
    QWidget *parent) {
  return new CuteQDockWidgetLayout(parent);
}

//  QDockWidgetLayout::~QDockWidgetLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDockWidgetLayoutD1Ev(QDockWidgetLayout *self) {
  delete self;
}

//  void QDockWidgetLayout::addItem(QLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDockWidgetLayout7addItemEP11QLayoutItem(
    QDockWidgetLayout *self,
    QLayoutItem *item) {
  self->addItem(item);
}

//  QLayoutItem *QDockWidgetLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK17QDockWidgetLayout6itemAtEi(
    const QDockWidgetLayout *self,
    int index) {
  return self->itemAt(index);
}

//  QLayoutItem *QDockWidgetLayout::takeAt(int index)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN17QDockWidgetLayout6takeAtEi(
    QDockWidgetLayout *self,
    int index) {
  return self->takeAt(index);
}

//  int QDockWidgetLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QDockWidgetLayout5countEv(const QDockWidgetLayout *self) {
  return self->count();
}

//  QSize QDockWidgetLayout::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QDockWidgetLayout11maximumSizeEv(
    const QDockWidgetLayout *self) {
  return new QSize(self->maximumSize());
}

//  QSize QDockWidgetLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QDockWidgetLayout11minimumSizeEv(
    const QDockWidgetLayout *self) {
  return new QSize(self->minimumSize());
}

//  QSize QDockWidgetLayout::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QDockWidgetLayout8sizeHintEv(
    const QDockWidgetLayout *self) {
  return new QSize(self->sizeHint());
}

//  QSize QDockWidgetLayout::sizeFromContent(const QSize &content, bool
//      floating) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QDockWidgetLayout15sizeFromContentERK5QSizeb(
    const QDockWidgetLayout *self,
    const QSize *content,
    bool floating) {
  return new QSize(self->sizeFromContent(*content, floating));
}

//  void QDockWidgetLayout::setGeometry(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDockWidgetLayout11setGeometryERK5QRect(
    QDockWidgetLayout *self,
    const QRect *r) {
  self->setGeometry(*r);
}

//  QWidget *QDockWidgetLayout::widgetForRole(Role r) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK17QDockWidgetLayout13widgetForRoleENS_4RoleE(
    const QDockWidgetLayout *self,
    QDockWidgetLayout::Role r) {
  return self->widgetForRole(r);
}

//  void QDockWidgetLayout::setWidgetForRole(Role r, QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDockWidgetLayout16setWidgetForRoleENS_4RoleEP7QWidget(
    QDockWidgetLayout *self,
    QDockWidgetLayout::Role r,
    QWidget *w) {
  self->setWidgetForRole(r, w);
}

//  QLayoutItem *QDockWidgetLayout::itemForRole(Role r) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK17QDockWidgetLayout11itemForRoleENS_4RoleE(
    const QDockWidgetLayout *self,
    QDockWidgetLayout::Role r) {
  return self->itemForRole(r);
}

//  QRect QDockWidgetLayout::titleArea() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK17QDockWidgetLayout9titleAreaEv(
    const QDockWidgetLayout *self) {
  return new QRect(self->titleArea());
}

//  int QDockWidgetLayout::minimumTitleWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QDockWidgetLayout17minimumTitleWidthEv(
    const QDockWidgetLayout *self) {
  return self->minimumTitleWidth();
}

//  int QDockWidgetLayout::titleHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QDockWidgetLayout11titleHeightEv(
    const QDockWidgetLayout *self) {
  return self->titleHeight();
}

//  bool QDockWidgetLayout::wmSupportsNativeWindowDeco()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QDockWidgetLayout26wmSupportsNativeWindowDecoEv() {
  return QDockWidgetLayout::wmSupportsNativeWindowDeco();
}

//  bool QDockWidgetLayout::nativeWindowDeco() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QDockWidgetLayout16nativeWindowDecoEv(
    const QDockWidgetLayout *self) {
  return self->nativeWindowDeco();
}

//  bool QDockWidgetLayout::nativeWindowDeco(bool floating) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QDockWidgetLayout16nativeWindowDecoEb(
    const QDockWidgetLayout *self,
    bool floating) {
  return self->nativeWindowDeco(floating);
}

//  void QDockWidgetLayout::setVerticalTitleBar(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDockWidgetLayout19setVerticalTitleBarEb(
    QDockWidgetLayout *self,
    bool b) {
  self->setVerticalTitleBar(b);
}

//  a Python function taken by a CuteQDockWidgetLayout, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDockWidgetLayout(
    QDockWidgetLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDockWidgetLayout *>(self)->take(key, call);
}

//  void QDockWidgetLayout::addItem(QLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QDockWidgetLayout7addItemEP11QLayoutItem(
    QDockWidgetLayout *self,
    QLayoutItem *item) {
  self->QDockWidgetLayout::addItem(item);
}

//  QLayoutItem *QDockWidgetLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_own_ZNK17QDockWidgetLayout6itemAtEi(
    const QDockWidgetLayout *self,
    int index) {
  return self->QDockWidgetLayout::itemAt(index);
}

//  QLayoutItem *QDockWidgetLayout::takeAt(int index)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_own_ZN17QDockWidgetLayout6takeAtEi(
    QDockWidgetLayout *self,
    int index) {
  return self->QDockWidgetLayout::takeAt(index);
}

//  int QDockWidgetLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QDockWidgetLayout5countEv(
    const QDockWidgetLayout *self) {
  return self->QDockWidgetLayout::count();
}

//  QSize QDockWidgetLayout::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK17QDockWidgetLayout11maximumSizeEv(
    const QDockWidgetLayout *self) {
  return new QSize(self->QDockWidgetLayout::maximumSize());
}

//  QSize QDockWidgetLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK17QDockWidgetLayout11minimumSizeEv(
    const QDockWidgetLayout *self) {
  return new QSize(self->QDockWidgetLayout::minimumSize());
}

//  QSize QDockWidgetLayout::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK17QDockWidgetLayout8sizeHintEv(
    const QDockWidgetLayout *self) {
  return new QSize(self->QDockWidgetLayout::sizeHint());
}

//  void QDockWidgetLayout::setGeometry(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QDockWidgetLayout11setGeometryERK5QRect(
    QDockWidgetLayout *self,
    const QRect *r) {
  self->QDockWidgetLayout::setGeometry(*r);
}

#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(dockwidget)
