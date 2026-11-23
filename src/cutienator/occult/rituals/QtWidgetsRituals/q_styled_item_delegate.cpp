//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleditemdelegate.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleditemdelegate.h>
#include <QtCore/qstring.h>
#include <QtWidgets/qstyleoption.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlocale.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QStyledItemDelegate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQStyledItemDelegate : QStyledItemDelegate {
  using QStyledItemDelegate::initStyleOption;
  using QStyledItemDelegate::eventFilter;
  using QStyledItemDelegate::editorEvent;
};

//  A QStyledItemDelegate that Python can take functions over in. Every QStyledItemDelegate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQStyledItemDelegateCall0)(const void *, QPainter *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef const QSize * (*CuteQStyledItemDelegateCall1)(const void *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef void * (*CuteQStyledItemDelegateCall2)(const void *, QWidget *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef void (*CuteQStyledItemDelegateCall3)(const void *, QWidget *, const QModelIndex *, int *);
typedef void (*CuteQStyledItemDelegateCall4)(const void *, QWidget *, QAbstractItemModel *, const QModelIndex *, int *);
typedef void (*CuteQStyledItemDelegateCall5)(const void *, QWidget *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef QString * (*CuteQStyledItemDelegateCall6)(const void *, const QVariant *, const QLocale *, int *);
typedef void (*CuteQStyledItemDelegateCall7)(const void *, QStyleOptionViewItem *, const QModelIndex *, int *);
typedef bool (*CuteQStyledItemDelegateCall8)(const void *, QObject *, QEvent *, int *);
typedef bool (*CuteQStyledItemDelegateCall9)(const void *, QEvent *, QAbstractItemModel *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef void (*CuteQStyledItemDelegateCall10)(const void *, QWidget *, const QModelIndex *, int *);
typedef bool (*CuteQStyledItemDelegateCall11)(const void *, QHelpEvent *, QAbstractItemView *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef bool (*CuteQStyledItemDelegateCall12)(const void *, QEvent *, int *);
typedef void (*CuteQStyledItemDelegateCall13)(const void *, QTimerEvent *, int *);
typedef void (*CuteQStyledItemDelegateCall14)(const void *, QChildEvent *, int *);
typedef void (*CuteQStyledItemDelegateCall15)(const void *, QEvent *, int *);
typedef void (*CuteQStyledItemDelegateCall16)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQStyledItemDelegateCall17)(const void *, const QMetaMethod *, int *);
class CuteQStyledItemDelegate : public QStyledItemDelegate {
public:
  using QStyledItemDelegate::QStyledItemDelegate;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate12createEditorEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate13setEditorDataEP7QWidgetRK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate12setModelDataEP7QWidgetP18QAbstractItemModelRK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate20updateEditorGeometryEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QStyledItemDelegate11displayTextERK8QVariantRK7QLocale")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QStyledItemDelegate15initStyleOptionEP20QStyleOptionViewItemRK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractItemDelegate11editorEventEP6QEventP18QAbstractItemModelRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate13destroyEditorEP7QWidgetRK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractItemDelegate9helpEventEP10QHelpEventP17QAbstractItemViewRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

  //  void QStyledItemDelegate::paint(QPainter *painter, const
  //      QStyleOptionViewItem &option, const QModelIndex &index) const
  void paint(
      QPainter *painter,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQStyledItemDelegateCall0 call = reinterpret_cast<CuteQStyledItemDelegateCall0>(taken[0]);
      call(this, painter, &option, &index, &handled);
      if (handled) return;
    }
    QStyledItemDelegate::paint(painter, option, index);
  }

  //  QSize QStyledItemDelegate::sizeHint(const QStyleOptionViewItem
  //      &option, const QModelIndex &index) const
  QSize sizeHint(
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQStyledItemDelegateCall1 call = reinterpret_cast<CuteQStyledItemDelegateCall1>(taken[1]);
      const QSize * given = call(this, &option, &index, &handled);
      if (handled && given) return *given;
    }
    return QStyledItemDelegate::sizeHint(option, index);
  }

  //  QWidget *QStyledItemDelegate::createEditor(QWidget *parent, const
  //      QStyleOptionViewItem &option, const QModelIndex &index) const
  QWidget *createEditor(
      QWidget *parent,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQStyledItemDelegateCall2 call = reinterpret_cast<CuteQStyledItemDelegateCall2>(taken[2]);
      void * given = call(this, parent, &option, &index, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QStyledItemDelegate::createEditor(parent, option, index);
  }

  //  void QStyledItemDelegate::setEditorData(QWidget *editor, const
  //      QModelIndex &index) const
  void setEditorData(
      QWidget *editor,
      const QModelIndex &index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQStyledItemDelegateCall3 call = reinterpret_cast<CuteQStyledItemDelegateCall3>(taken[3]);
      call(this, editor, &index, &handled);
      if (handled) return;
    }
    QStyledItemDelegate::setEditorData(editor, index);
  }

  //  void QStyledItemDelegate::setModelData(QWidget *editor,
  //      QAbstractItemModel *model, const QModelIndex &index) const
  void setModelData(
      QWidget *editor,
      QAbstractItemModel *model,
      const QModelIndex &index) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQStyledItemDelegateCall4 call = reinterpret_cast<CuteQStyledItemDelegateCall4>(taken[4]);
      call(this, editor, model, &index, &handled);
      if (handled) return;
    }
    QStyledItemDelegate::setModelData(editor, model, index);
  }

  //  void QStyledItemDelegate::updateEditorGeometry(QWidget *editor, const
  //      QStyleOptionViewItem &option, const QModelIndex &index) const
  void updateEditorGeometry(
      QWidget *editor,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQStyledItemDelegateCall5 call = reinterpret_cast<CuteQStyledItemDelegateCall5>(taken[5]);
      call(this, editor, &option, &index, &handled);
      if (handled) return;
    }
    QStyledItemDelegate::updateEditorGeometry(editor, option, index);
  }

  //  QString QStyledItemDelegate::displayText(const QVariant &value, const
  //      QLocale &locale) const
  QString displayText(
      const QVariant &value,
      const QLocale &locale) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQStyledItemDelegateCall6 call = reinterpret_cast<CuteQStyledItemDelegateCall6>(taken[6]);
      QString * given = call(this, &value, &locale, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QStyledItemDelegate::displayText(value, locale);
  }

  //  void QStyledItemDelegate::initStyleOption(QStyleOptionViewItem
  //      *option, const QModelIndex &index) const
  void initStyleOption(
      QStyleOptionViewItem *option,
      const QModelIndex &index) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQStyledItemDelegateCall7 call = reinterpret_cast<CuteQStyledItemDelegateCall7>(taken[7]);
      call(this, option, &index, &handled);
      if (handled) return;
    }
    QStyledItemDelegate::initStyleOption(option, index);
  }

  //  bool QStyledItemDelegate::eventFilter(QObject *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQStyledItemDelegateCall8 call = reinterpret_cast<CuteQStyledItemDelegateCall8>(taken[8]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QStyledItemDelegate::eventFilter(object, event);
  }

  //  bool QStyledItemDelegate::editorEvent(QEvent *event,
  //      QAbstractItemModel *model, const QStyleOptionViewItem &option,
  //      const QModelIndex &index)
  bool editorEvent(
      QEvent *event,
      QAbstractItemModel *model,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) override {
    if (taken[9]) {
      int handled = 0;
      CuteQStyledItemDelegateCall9 call = reinterpret_cast<CuteQStyledItemDelegateCall9>(taken[9]);
      bool given = call(this, event, model, &option, &index, &handled);
      if (handled) return given;
    }
    return QStyledItemDelegate::editorEvent(event, model, option, index);
  }

  //  void QAbstractItemDelegate::destroyEditor(QWidget *editor, const
  //      QModelIndex &index) const
  void destroyEditor(
      QWidget *editor,
      const QModelIndex &index) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQStyledItemDelegateCall10 call = reinterpret_cast<CuteQStyledItemDelegateCall10>(taken[10]);
      call(this, editor, &index, &handled);
      if (handled) return;
    }
    QAbstractItemDelegate::destroyEditor(editor, index);
  }

  //  bool QAbstractItemDelegate::helpEvent(QHelpEvent *event,
  //      QAbstractItemView *view, const QStyleOptionViewItem &option,
  //      const QModelIndex &index)
  bool helpEvent(
      QHelpEvent *event,
      QAbstractItemView *view,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) override {
    if (taken[11]) {
      int handled = 0;
      CuteQStyledItemDelegateCall11 call = reinterpret_cast<CuteQStyledItemDelegateCall11>(taken[11]);
      bool given = call(this, event, view, &option, &index, &handled);
      if (handled) return given;
    }
    return QAbstractItemDelegate::helpEvent(event, view, option, index);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQStyledItemDelegateCall12 call = reinterpret_cast<CuteQStyledItemDelegateCall12>(taken[12]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQStyledItemDelegateCall13 call = reinterpret_cast<CuteQStyledItemDelegateCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQStyledItemDelegateCall14 call = reinterpret_cast<CuteQStyledItemDelegateCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQStyledItemDelegateCall15 call = reinterpret_cast<CuteQStyledItemDelegateCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQStyledItemDelegateCall16 call = reinterpret_cast<CuteQStyledItemDelegateCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQStyledItemDelegateCall17 call = reinterpret_cast<CuteQStyledItemDelegateCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QStyledItemDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QStyledItemDelegate10metaObjectEv(
    const QStyledItemDelegate *self) {
  return self->metaObject();
}

//  QString QStyledItemDelegate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QStyledItemDelegate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStyledItemDelegate::tr(s, c, n));
}

//  QStyledItemDelegate::QStyledItemDelegate(QObject *parent)
extern "C" Q_DECL_EXPORT
QStyledItemDelegate *ritual_ZN19QStyledItemDelegateC1EP7QObject(
    QObject *parent) {
  return new CuteQStyledItemDelegate(parent);
}

//  QStyledItemDelegate::~QStyledItemDelegate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QStyledItemDelegateD1Ev(QStyledItemDelegate *self) {
  delete self;
}

//  void QStyledItemDelegate::paint(QPainter *painter, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QStyledItemDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const QStyledItemDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->paint(painter, *option, *index);
}

//  QSize QStyledItemDelegate::sizeHint(const QStyleOptionViewItem &option,
//      const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QStyledItemDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex(
    const QStyledItemDelegate *self,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return new QSize(self->sizeHint(*option, *index));
}

//  QWidget *QStyledItemDelegate::createEditor(QWidget *parent, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK19QStyledItemDelegate12createEditorEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex(
    const QStyledItemDelegate *self,
    QWidget *parent,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return self->createEditor(parent, *option, *index);
}

//  void QStyledItemDelegate::setEditorData(QWidget *editor, const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QStyledItemDelegate13setEditorDataEP7QWidgetRK11QModelIndex(
    const QStyledItemDelegate *self,
    QWidget *editor,
    const QModelIndex *index) {
  self->setEditorData(editor, *index);
}

//  void QStyledItemDelegate::setModelData(QWidget *editor,
//      QAbstractItemModel *model, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QStyledItemDelegate12setModelDataEP7QWidgetP18QAbstractItemModelRK11QModelIndex(
    const QStyledItemDelegate *self,
    QWidget *editor,
    QAbstractItemModel *model,
    const QModelIndex *index) {
  self->setModelData(editor, model, *index);
}

//  void QStyledItemDelegate::updateEditorGeometry(QWidget *editor, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QStyledItemDelegate20updateEditorGeometryEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex(
    const QStyledItemDelegate *self,
    QWidget *editor,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->updateEditorGeometry(editor, *option, *index);
}

//  QItemEditorFactory *QStyledItemDelegate::itemEditorFactory() const
extern "C" Q_DECL_EXPORT
QItemEditorFactory *ritual_ZNK19QStyledItemDelegate17itemEditorFactoryEv(
    const QStyledItemDelegate *self) {
  return self->itemEditorFactory();
}

//  void QStyledItemDelegate::setItemEditorFactory(QItemEditorFactory
//      *factory)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QStyledItemDelegate20setItemEditorFactoryEP18QItemEditorFactory(
    QStyledItemDelegate *self,
    QItemEditorFactory *factory) {
  self->setItemEditorFactory(factory);
}

//  QString QStyledItemDelegate::displayText(const QVariant &value, const
//      QLocale &locale) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QStyledItemDelegate11displayTextERK8QVariantRK7QLocale(
    const QStyledItemDelegate *self,
    const QVariant *value,
    const QLocale *locale) {
  return new QString(self->displayText(*value, *locale));
}

//  void QStyledItemDelegate::initStyleOption(QStyleOptionViewItem *option,
//      const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QStyledItemDelegate15initStyleOptionEP20QStyleOptionViewItemRK11QModelIndex(
    const QStyledItemDelegate *self,
    QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->initStyleOption(option, *index);
}

//  bool QStyledItemDelegate::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QStyledItemDelegate11eventFilterEP7QObjectP6QEvent(
    QStyledItemDelegate *self,
    QObject *object,
    QEvent *event) {
  return self->eventFilter(object, event);
}

//  bool QStyledItemDelegate::editorEvent(QEvent *event, QAbstractItemModel
//      *model, const QStyleOptionViewItem &option, const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QStyledItemDelegate11editorEventEP6QEventP18QAbstractItemModelRK20QStyleOptionViewItemRK11QModelIndex(
    QStyledItemDelegate *self,
    QEvent *event,
    QAbstractItemModel *model,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return self->editorEvent(event, model, *option, *index);
}

//  a Python function taken by a CuteQStyledItemDelegate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStyledItemDelegate(
    QStyledItemDelegate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQStyledItemDelegate *>(self)->take(key, call);
}

//  void QStyledItemDelegate::paint(QPainter *painter, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK19QStyledItemDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const QStyledItemDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->QStyledItemDelegate::paint(painter, *option, *index);
}

//  QSize QStyledItemDelegate::sizeHint(const QStyleOptionViewItem &option,
//      const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK19QStyledItemDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex(
    const QStyledItemDelegate *self,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return new QSize(self->QStyledItemDelegate::sizeHint(*option, *index));
}

//  QWidget *QStyledItemDelegate::createEditor(QWidget *parent, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZNK19QStyledItemDelegate12createEditorEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex(
    const QStyledItemDelegate *self,
    QWidget *parent,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return self->QStyledItemDelegate::createEditor(parent, *option, *index);
}

//  void QStyledItemDelegate::setEditorData(QWidget *editor, const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK19QStyledItemDelegate13setEditorDataEP7QWidgetRK11QModelIndex(
    const QStyledItemDelegate *self,
    QWidget *editor,
    const QModelIndex *index) {
  self->QStyledItemDelegate::setEditorData(editor, *index);
}

//  void QStyledItemDelegate::setModelData(QWidget *editor,
//      QAbstractItemModel *model, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK19QStyledItemDelegate12setModelDataEP7QWidgetP18QAbstractItemModelRK11QModelIndex(
    const QStyledItemDelegate *self,
    QWidget *editor,
    QAbstractItemModel *model,
    const QModelIndex *index) {
  self->QStyledItemDelegate::setModelData(editor, model, *index);
}

//  void QStyledItemDelegate::updateEditorGeometry(QWidget *editor, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK19QStyledItemDelegate20updateEditorGeometryEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex(
    const QStyledItemDelegate *self,
    QWidget *editor,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->QStyledItemDelegate::updateEditorGeometry(editor, *option, *index);
}

//  QString QStyledItemDelegate::displayText(const QVariant &value, const
//      QLocale &locale) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK19QStyledItemDelegate11displayTextERK8QVariantRK7QLocale(
    const QStyledItemDelegate *self,
    const QVariant *value,
    const QLocale *locale) {
  return new QString(
      self->QStyledItemDelegate::displayText(
          *value,
          *locale));
}

//  void QStyledItemDelegate::initStyleOption(QStyleOptionViewItem *option,
//      const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK19QStyledItemDelegate15initStyleOptionEP20QStyleOptionViewItemRK11QModelIndex(
    const QStyledItemDelegate *self,
    QStyleOptionViewItem *option,
    const QModelIndex *index) {
  static_cast<const OwnQStyledItemDelegate *>(self)->OwnQStyledItemDelegate::initStyleOption(
      option,
      *index);
}

//  bool QStyledItemDelegate::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QStyledItemDelegate11eventFilterEP7QObjectP6QEvent(
    QStyledItemDelegate *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQStyledItemDelegate *>(self)->OwnQStyledItemDelegate::eventFilter(
      object,
      event);
}

//  bool QStyledItemDelegate::editorEvent(QEvent *event, QAbstractItemModel
//      *model, const QStyleOptionViewItem &option, const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QStyledItemDelegate11editorEventEP6QEventP18QAbstractItemModelRK20QStyleOptionViewItemRK11QModelIndex(
    QStyledItemDelegate *self,
    QEvent *event,
    QAbstractItemModel *model,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return static_cast<OwnQStyledItemDelegate *>(self)->OwnQStyledItemDelegate::editorEvent(
      event,
      model,
      *option,
      *index);
}
