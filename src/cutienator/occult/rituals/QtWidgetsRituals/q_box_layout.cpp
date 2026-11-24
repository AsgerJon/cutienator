//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qboxlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qboxlayout.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QBoxLayout that Python can take functions over in. Every QBoxLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQBoxLayoutCall0)(const void *, QLayoutItem *, int *);
typedef int (*CuteQBoxLayoutCall1)(const void *, int *);
typedef void (*CuteQBoxLayoutCall2)(const void *, int, int *);
typedef const QSize * (*CuteQBoxLayoutCall3)(const void *, int *);
typedef const QSize * (*CuteQBoxLayoutCall4)(const void *, int *);
typedef const QSize * (*CuteQBoxLayoutCall5)(const void *, int *);
typedef bool (*CuteQBoxLayoutCall6)(const void *, int *);
typedef int (*CuteQBoxLayoutCall7)(const void *, int, int *);
typedef int (*CuteQBoxLayoutCall8)(const void *, int, int *);
typedef int (*CuteQBoxLayoutCall9)(const void *, int *);
typedef void (*CuteQBoxLayoutCall10)(const void *, int *);
typedef void * (*CuteQBoxLayoutCall11)(const void *, int, int *);
typedef void * (*CuteQBoxLayoutCall12)(const void *, int, int *);
typedef int (*CuteQBoxLayoutCall13)(const void *, int *);
typedef void (*CuteQBoxLayoutCall14)(const void *, const QRect *, int *);
typedef const QRect * (*CuteQBoxLayoutCall15)(const void *, int *);
typedef int (*CuteQBoxLayoutCall16)(const void *, const QWidget *, int *);
typedef int (*CuteQBoxLayoutCall17)(const void *, const QLayoutItem *, int *);
typedef bool (*CuteQBoxLayoutCall18)(const void *, int *);
typedef int (*CuteQBoxLayoutCall19)(const void *, int *);
typedef void * (*CuteQBoxLayoutCall20)(const void *, QWidget *, QWidget *, int, int *);
typedef void * (*CuteQBoxLayoutCall21)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxLayoutCall22)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBoxLayoutCall23)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBoxLayoutCall24)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxLayoutCall25)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxLayoutCall26)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxLayoutCall27)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxLayoutCall28)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQBoxLayoutCall29)(const void *, int *);
typedef void * (*CuteQBoxLayoutCall30)(const void *, int *);
class CuteQBoxLayout : public QBoxLayout {
public:
  using QBoxLayout::QBoxLayout;
  void *taken[31] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QLayout7addItemEP11QLayoutItem")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7spacingEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout10setSpacingEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem8sizeHintEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem11minimumSizeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem11maximumSizeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem17hasHeightForWidthEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem14heightForWidthEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem21minimumHeightForWidthEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem19expandingDirectionsEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem10invalidateEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout6itemAtEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout6takeAtEi")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout5countEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem11setGeometryERK5QRect")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem8geometryEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7indexOfEPK7QWidget")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7indexOfEPK11QLayoutItem")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem7isEmptyEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem12controlTypesEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout13replaceWidgetEP7QWidgetS1_6QFlagsIN2Qt15FindChildOptionEE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem6layoutEv")) {
      taken[21] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
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

  //  void QBoxLayout::addItem(QLayoutItem *a0)
  void addItem(QLayoutItem *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQBoxLayoutCall0 call = reinterpret_cast<CuteQBoxLayoutCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QBoxLayout::addItem(a0);
  }

  //  int QBoxLayout::spacing() const
  int spacing() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQBoxLayoutCall1 call = reinterpret_cast<CuteQBoxLayoutCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QBoxLayout::spacing();
  }

  //  void QBoxLayout::setSpacing(int spacing)
  void setSpacing(int spacing) override {
    if (taken[2]) {
      int handled = 0;
      CuteQBoxLayoutCall2 call = reinterpret_cast<CuteQBoxLayoutCall2>(taken[2]);
      call(this, spacing, &handled);
      if (handled) return;
    }
    QBoxLayout::setSpacing(spacing);
  }

  //  QSize QBoxLayout::sizeHint() const
  QSize sizeHint() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQBoxLayoutCall3 call = reinterpret_cast<CuteQBoxLayoutCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QBoxLayout::sizeHint();
  }

  //  QSize QBoxLayout::minimumSize() const
  QSize minimumSize() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQBoxLayoutCall4 call = reinterpret_cast<CuteQBoxLayoutCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QBoxLayout::minimumSize();
  }

  //  QSize QBoxLayout::maximumSize() const
  QSize maximumSize() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQBoxLayoutCall5 call = reinterpret_cast<CuteQBoxLayoutCall5>(taken[5]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QBoxLayout::maximumSize();
  }

  //  bool QBoxLayout::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQBoxLayoutCall6 call = reinterpret_cast<CuteQBoxLayoutCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QBoxLayout::hasHeightForWidth();
  }

  //  int QBoxLayout::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQBoxLayoutCall7 call = reinterpret_cast<CuteQBoxLayoutCall7>(taken[7]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QBoxLayout::heightForWidth(a0);
  }

  //  int QBoxLayout::minimumHeightForWidth(int a0) const
  int minimumHeightForWidth(int a0) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQBoxLayoutCall8 call = reinterpret_cast<CuteQBoxLayoutCall8>(taken[8]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QBoxLayout::minimumHeightForWidth(a0);
  }

  //  Qt::Orientations QBoxLayout::expandingDirections() const
  Qt::Orientations expandingDirections() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQBoxLayoutCall9 call = reinterpret_cast<CuteQBoxLayoutCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::Orientation>::fromInt(given);
    }
    return QBoxLayout::expandingDirections();
  }

  //  void QBoxLayout::invalidate()
  void invalidate() override {
    if (taken[10]) {
      int handled = 0;
      CuteQBoxLayoutCall10 call = reinterpret_cast<CuteQBoxLayoutCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QBoxLayout::invalidate();
  }

  //  QLayoutItem *QBoxLayout::itemAt(int a0) const
  QLayoutItem *itemAt(int a0) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQBoxLayoutCall11 call = reinterpret_cast<CuteQBoxLayoutCall11>(taken[11]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QBoxLayout::itemAt(a0);
  }

  //  QLayoutItem *QBoxLayout::takeAt(int a0)
  QLayoutItem *takeAt(int a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQBoxLayoutCall12 call = reinterpret_cast<CuteQBoxLayoutCall12>(taken[12]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QBoxLayout::takeAt(a0);
  }

  //  int QBoxLayout::count() const
  int count() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQBoxLayoutCall13 call = reinterpret_cast<CuteQBoxLayoutCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QBoxLayout::count();
  }

  //  void QBoxLayout::setGeometry(const QRect &a0)
  void setGeometry(const QRect &a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQBoxLayoutCall14 call = reinterpret_cast<CuteQBoxLayoutCall14>(taken[14]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QBoxLayout::setGeometry(a0);
  }

  //  QRect QLayout::geometry() const
  QRect geometry() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQBoxLayoutCall15 call = reinterpret_cast<CuteQBoxLayoutCall15>(taken[15]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLayout::geometry();
  }

  //  int QLayout::indexOf(const QWidget *a0) const
  int indexOf(const QWidget *a0) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQBoxLayoutCall16 call = reinterpret_cast<CuteQBoxLayoutCall16>(taken[16]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  int QLayout::indexOf(const QLayoutItem *a0) const
  int indexOf(const QLayoutItem *a0) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQBoxLayoutCall17 call = reinterpret_cast<CuteQBoxLayoutCall17>(taken[17]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  bool QLayout::isEmpty() const
  bool isEmpty() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQBoxLayoutCall18 call = reinterpret_cast<CuteQBoxLayoutCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLayout::isEmpty();
  }

  //  QSizePolicy::ControlTypes QLayout::controlTypes() const
  QSizePolicy::ControlTypes controlTypes() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQBoxLayoutCall19 call = reinterpret_cast<CuteQBoxLayoutCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQBoxLayoutCall20 call = reinterpret_cast<CuteQBoxLayoutCall20>(taken[20]);
      void * given = call(this, from, to, static_cast<int>(options.toInt()), &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QLayout::replaceWidget(from, to, options);
  }

  //  QLayout *QLayout::layout()
  QLayout *layout() override {
    if (taken[21]) {
      int handled = 0;
      CuteQBoxLayoutCall21 call = reinterpret_cast<CuteQBoxLayoutCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QLayout::layout();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QLayout::childEvent(QChildEvent *e)
  void childEvent(QChildEvent *e) override {
    if (taken[22]) {
      int handled = 0;
      CuteQBoxLayoutCall22 call = reinterpret_cast<CuteQBoxLayoutCall22>(taken[22]);
      call(this, e, &handled);
      if (handled) return;
    }
    QLayout::childEvent(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQBoxLayoutCall23 call = reinterpret_cast<CuteQBoxLayoutCall23>(taken[23]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQBoxLayoutCall24 call = reinterpret_cast<CuteQBoxLayoutCall24>(taken[24]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQBoxLayoutCall25 call = reinterpret_cast<CuteQBoxLayoutCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQBoxLayoutCall26 call = reinterpret_cast<CuteQBoxLayoutCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[27]) {
      int handled = 0;
      CuteQBoxLayoutCall27 call = reinterpret_cast<CuteQBoxLayoutCall27>(taken[27]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[28]) {
      int handled = 0;
      CuteQBoxLayoutCall28 call = reinterpret_cast<CuteQBoxLayoutCall28>(taken[28]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QWidget *QLayoutItem::widget() const
  QWidget *widget() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQBoxLayoutCall29 call = reinterpret_cast<CuteQBoxLayoutCall29>(taken[29]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QLayoutItem::widget();
  }

  //  QSpacerItem *QLayoutItem::spacerItem()
  QSpacerItem *spacerItem() override {
    if (taken[30]) {
      int handled = 0;
      CuteQBoxLayoutCall30 call = reinterpret_cast<CuteQBoxLayoutCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSpacerItem *>(given);
    }
    return QLayoutItem::spacerItem();
  }
};

//  const QMetaObject *QBoxLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QBoxLayout10metaObjectEv(
    const QBoxLayout *self) {
  return self->metaObject();
}

//  QString QBoxLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QBoxLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBoxLayout::tr(s, c, n));
}

//  QBoxLayout::QBoxLayout(Direction a0, QWidget *parent)
extern "C" Q_DECL_EXPORT
QBoxLayout *ritual_ZN10QBoxLayoutC1ENS_9DirectionEP7QWidget(
    QBoxLayout::Direction a0,
    QWidget *parent) {
  return new CuteQBoxLayout(a0, parent);
}

//  QBoxLayout::~QBoxLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayoutD1Ev(QBoxLayout *self) {
  delete self;
}

//  Direction QBoxLayout::direction() const
extern "C" Q_DECL_EXPORT
QBoxLayout::Direction ritual_ZNK10QBoxLayout9directionEv(
    const QBoxLayout *self) {
  return self->direction();
}

//  void QBoxLayout::setDirection(Direction a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout12setDirectionENS_9DirectionE(
    QBoxLayout *self,
    QBoxLayout::Direction a0) {
  self->setDirection(a0);
}

//  void QBoxLayout::addSpacing(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout10addSpacingEi(QBoxLayout *self, int size) {
  self->addSpacing(size);
}

//  void QBoxLayout::addStretch(int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout10addStretchEi(QBoxLayout *self, int stretch) {
  self->addStretch(stretch);
}

//  void QBoxLayout::addSpacerItem(QSpacerItem *spacerItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout13addSpacerItemEP11QSpacerItem(
    QBoxLayout *self,
    QSpacerItem *spacerItem) {
  self->addSpacerItem(spacerItem);
}

//  void QBoxLayout::addWidget(QWidget *a0, int stretch, Qt::Alignment
//      alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout9addWidgetEP7QWidgeti6QFlagsIN2Qt13AlignmentFlagEE(
    QBoxLayout *self,
    QWidget *a0,
    int stretch,
    int alignment) {
  self->addWidget(
      a0,
      stretch,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void QBoxLayout::addLayout(QLayout *layout, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout9addLayoutEP7QLayouti(
    QBoxLayout *self,
    QLayout *layout,
    int stretch) {
  self->addLayout(layout, stretch);
}

//  void QBoxLayout::addStrut(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout8addStrutEi(QBoxLayout *self, int a0) {
  self->addStrut(a0);
}

//  void QBoxLayout::addItem(QLayoutItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout7addItemEP11QLayoutItem(
    QBoxLayout *self,
    QLayoutItem *a0) {
  self->addItem(a0);
}

//  void QBoxLayout::insertSpacing(int index, int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout13insertSpacingEii(
    QBoxLayout *self,
    int index,
    int size) {
  self->insertSpacing(index, size);
}

//  void QBoxLayout::insertStretch(int index, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout13insertStretchEii(
    QBoxLayout *self,
    int index,
    int stretch) {
  self->insertStretch(index, stretch);
}

//  void QBoxLayout::insertSpacerItem(int index, QSpacerItem *spacerItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout16insertSpacerItemEiP11QSpacerItem(
    QBoxLayout *self,
    int index,
    QSpacerItem *spacerItem) {
  self->insertSpacerItem(index, spacerItem);
}

//  void QBoxLayout::insertWidget(int index, QWidget *widget, int stretch,
//      Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout12insertWidgetEiP7QWidgeti6QFlagsIN2Qt13AlignmentFlagEE(
    QBoxLayout *self,
    int index,
    QWidget *widget,
    int stretch,
    int alignment) {
  self->insertWidget(
      index,
      widget,
      stretch,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void QBoxLayout::insertLayout(int index, QLayout *layout, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout12insertLayoutEiP7QLayouti(
    QBoxLayout *self,
    int index,
    QLayout *layout,
    int stretch) {
  self->insertLayout(index, layout, stretch);
}

//  void QBoxLayout::insertItem(int index, QLayoutItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout10insertItemEiP11QLayoutItem(
    QBoxLayout *self,
    int index,
    QLayoutItem *a1) {
  self->insertItem(index, a1);
}

//  int QBoxLayout::spacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QBoxLayout7spacingEv(const QBoxLayout *self) {
  return self->spacing();
}

//  void QBoxLayout::setSpacing(int spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout10setSpacingEi(QBoxLayout *self, int spacing) {
  self->setSpacing(spacing);
}

//  bool QBoxLayout::setStretchFactor(QWidget *w, int stretch)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QBoxLayout16setStretchFactorEP7QWidgeti(
    QBoxLayout *self,
    QWidget *w,
    int stretch) {
  return self->setStretchFactor(w, stretch);
}

//  bool QBoxLayout::setStretchFactor(QLayout *l, int stretch)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QBoxLayout16setStretchFactorEP7QLayouti(
    QBoxLayout *self,
    QLayout *l,
    int stretch) {
  return self->setStretchFactor(l, stretch);
}

//  void QBoxLayout::setStretch(int index, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout10setStretchEii(
    QBoxLayout *self,
    int index,
    int stretch) {
  self->setStretch(index, stretch);
}

//  int QBoxLayout::stretch(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QBoxLayout7stretchEi(const QBoxLayout *self, int index) {
  return self->stretch(index);
}

//  QSize QBoxLayout::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QBoxLayout8sizeHintEv(const QBoxLayout *self) {
  return new QSize(self->sizeHint());
}

//  QSize QBoxLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QBoxLayout11minimumSizeEv(const QBoxLayout *self) {
  return new QSize(self->minimumSize());
}

//  QSize QBoxLayout::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QBoxLayout11maximumSizeEv(const QBoxLayout *self) {
  return new QSize(self->maximumSize());
}

//  bool QBoxLayout::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QBoxLayout17hasHeightForWidthEv(const QBoxLayout *self) {
  return self->hasHeightForWidth();
}

//  int QBoxLayout::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QBoxLayout14heightForWidthEi(
    const QBoxLayout *self,
    int a0) {
  return self->heightForWidth(a0);
}

//  int QBoxLayout::minimumHeightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QBoxLayout21minimumHeightForWidthEi(
    const QBoxLayout *self,
    int a0) {
  return self->minimumHeightForWidth(a0);
}

//  Qt::Orientations QBoxLayout::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QBoxLayout19expandingDirectionsEv(const QBoxLayout *self) {
  return static_cast<int>(self->expandingDirections().toInt());
}

//  void QBoxLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout10invalidateEv(QBoxLayout *self) {
  self->invalidate();
}

//  QLayoutItem *QBoxLayout::itemAt(int a0) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK10QBoxLayout6itemAtEi(
    const QBoxLayout *self,
    int a0) {
  return self->itemAt(a0);
}

//  QLayoutItem *QBoxLayout::takeAt(int a0)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN10QBoxLayout6takeAtEi(QBoxLayout *self, int a0) {
  return self->takeAt(a0);
}

//  int QBoxLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QBoxLayout5countEv(const QBoxLayout *self) {
  return self->count();
}

//  void QBoxLayout::setGeometry(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout11setGeometryERK5QRect(
    QBoxLayout *self,
    const QRect *a0) {
  self->setGeometry(*a0);
}

//  a Python function taken by a CuteQBoxLayout, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBoxLayout(QBoxLayout *self, const char *key, void *call) {
  return static_cast<CuteQBoxLayout *>(self)->take(key, call);
}

//  void QBoxLayout::addItem(QLayoutItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QBoxLayout7addItemEP11QLayoutItem(
    QBoxLayout *self,
    QLayoutItem *a0) {
  self->QBoxLayout::addItem(a0);
}

//  int QBoxLayout::spacing() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QBoxLayout7spacingEv(const QBoxLayout *self) {
  return self->QBoxLayout::spacing();
}

//  void QBoxLayout::setSpacing(int spacing)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QBoxLayout10setSpacingEi(QBoxLayout *self, int spacing) {
  self->QBoxLayout::setSpacing(spacing);
}

//  QSize QBoxLayout::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK10QBoxLayout8sizeHintEv(const QBoxLayout *self) {
  return new QSize(self->QBoxLayout::sizeHint());
}

//  QSize QBoxLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK10QBoxLayout11minimumSizeEv(const QBoxLayout *self) {
  return new QSize(self->QBoxLayout::minimumSize());
}

//  QSize QBoxLayout::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK10QBoxLayout11maximumSizeEv(const QBoxLayout *self) {
  return new QSize(self->QBoxLayout::maximumSize());
}

//  bool QBoxLayout::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QBoxLayout17hasHeightForWidthEv(
    const QBoxLayout *self) {
  return self->QBoxLayout::hasHeightForWidth();
}

//  int QBoxLayout::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QBoxLayout14heightForWidthEi(
    const QBoxLayout *self,
    int a0) {
  return self->QBoxLayout::heightForWidth(a0);
}

//  int QBoxLayout::minimumHeightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QBoxLayout21minimumHeightForWidthEi(
    const QBoxLayout *self,
    int a0) {
  return self->QBoxLayout::minimumHeightForWidth(a0);
}

//  Qt::Orientations QBoxLayout::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QBoxLayout19expandingDirectionsEv(
    const QBoxLayout *self) {
  return static_cast<int>(self->QBoxLayout::expandingDirections().toInt());
}

//  void QBoxLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QBoxLayout10invalidateEv(QBoxLayout *self) {
  self->QBoxLayout::invalidate();
}

//  QLayoutItem *QBoxLayout::itemAt(int a0) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_own_ZNK10QBoxLayout6itemAtEi(
    const QBoxLayout *self,
    int a0) {
  return self->QBoxLayout::itemAt(a0);
}

//  QLayoutItem *QBoxLayout::takeAt(int a0)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_own_ZN10QBoxLayout6takeAtEi(QBoxLayout *self, int a0) {
  return self->QBoxLayout::takeAt(a0);
}

//  int QBoxLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QBoxLayout5countEv(const QBoxLayout *self) {
  return self->QBoxLayout::count();
}

//  void QBoxLayout::setGeometry(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QBoxLayout11setGeometryERK5QRect(
    QBoxLayout *self,
    const QRect *a0) {
  self->QBoxLayout::setGeometry(*a0);
}
