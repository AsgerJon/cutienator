//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qaccessiblewidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#include <QtWidgets/qaccessiblewidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#include <QtGui/qcolor.h>
#include <cstring>
#include <QtCore/QList>
#include <QtGui/QAccessible>

//  A QAccessibleWidgetV2 that Python can take functions over in. Every QAccessibleWidgetV2
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleWidgetV2Call0)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleWidgetV2Call1)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleWidgetV2Call2)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleWidgetV2Call3)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleWidgetV2Call4)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleWidgetV2Call5)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleWidgetV2Call6)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleWidgetV2Call7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleWidgetV2Call8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleWidgetV2Call9)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleWidgetV2Call10)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleWidgetV2Call11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleWidgetV2Call12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleWidgetV2Call13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleWidgetV2Call14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleWidgetV2Call15)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleWidgetV2Call16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleWidgetV2Call17)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleWidgetV2Call18)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleWidgetV2Call19)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleWidgetV2Call20)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleWidgetV2Call21)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleWidgetV2 : public QAccessibleWidgetV2 {
public:
  using QAccessibleWidgetV2::QAccessibleWidgetV2;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface14interface_castEN11QAccessible13InterfaceTypeE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface12virtual_hookEiPv")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
  //  void *QAccessibleWidgetV2::interface_cast(QAccessible::InterfaceType
  //      t)
  void *interface_cast(QAccessible::InterfaceType t) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call0 call = reinterpret_cast<CuteQAccessibleWidgetV2Call0>(taken[0]);
      void * given = call(this, static_cast<int>(t), &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QAccessibleWidgetV2::interface_cast(t);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call1 call = reinterpret_cast<CuteQAccessibleWidgetV2Call1>(taken[1]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call2 call = reinterpret_cast<CuteQAccessibleWidgetV2Call2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call3 call = reinterpret_cast<CuteQAccessibleWidgetV2Call3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleWidget::childCount() const
  int childCount() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call4 call = reinterpret_cast<CuteQAccessibleWidgetV2Call4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::childCount();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleWidget::indexOfChild(const QAccessibleInterface
  //      *child) const
  int indexOfChild(const QAccessibleInterface *child) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call5 call = reinterpret_cast<CuteQAccessibleWidgetV2Call5>(taken[5]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::indexOfChild(child);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call6 call = reinterpret_cast<CuteQAccessibleWidgetV2Call6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call7 call = reinterpret_cast<CuteQAccessibleWidgetV2Call7>(taken[7]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call8 call = reinterpret_cast<CuteQAccessibleWidgetV2Call8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call9 call = reinterpret_cast<CuteQAccessibleWidgetV2Call9>(taken[9]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleWidget::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call10 call = reinterpret_cast<CuteQAccessibleWidgetV2Call10>(taken[10]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleWidget::text(t);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleWidget::role() const
  QAccessible::Role role() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call11 call = reinterpret_cast<CuteQAccessibleWidgetV2Call11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleWidget::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleWidget::state() const
  QAccessible::State state() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call12 call = reinterpret_cast<CuteQAccessibleWidgetV2Call12>(taken[12]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::state();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call13 call = reinterpret_cast<CuteQAccessibleWidgetV2Call13>(taken[13]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call14 call = reinterpret_cast<CuteQAccessibleWidgetV2Call14>(taken[14]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call15 call = reinterpret_cast<CuteQAccessibleWidgetV2Call15>(taken[15]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call16 call = reinterpret_cast<CuteQAccessibleWidgetV2Call16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QAccessibleObject::object();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleObject::setText(QAccessible::Text t, const QString
  //      &text)
  void setText(QAccessible::Text t, const QString &text) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call17 call = reinterpret_cast<CuteQAccessibleWidgetV2Call17>(taken[17]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call18 call = reinterpret_cast<CuteQAccessibleWidgetV2Call18>(taken[18]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleObject::childAt(x, y);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleInterface::virtual_hook(int id, void *data)
  void virtual_hook(int id, void *data) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call19 call = reinterpret_cast<CuteQAccessibleWidgetV2Call19>(taken[19]);
      call(this, id, data, &handled);
      if (handled) return;
    }
    QAccessibleInterface::virtual_hook(id, data);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionName(const QString
  //      &name) const
  QString localizedActionName(const QString &name) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call20 call = reinterpret_cast<CuteQAccessibleWidgetV2Call20>(taken[20]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleActionInterface::localizedActionName(name);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionDescription(const
  //      QString &name) const
  QString localizedActionDescription(const QString &name) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call21 call = reinterpret_cast<CuteQAccessibleWidgetV2Call21>(taken[21]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleActionInterface::localizedActionDescription(name);
  }
#endif  // QT_CONFIG(accessibility)
};

//  QAccessibleWidgetV2::QAccessibleWidgetV2(QWidget *object,
//      QAccessible::Role role)
extern "C" Q_DECL_EXPORT
QAccessibleWidgetV2 *ritual_ZN19QAccessibleWidgetV2C1EP7QWidgetN11QAccessible4RoleE(
    QWidget *object,
    QAccessible::Role role) {
  return new CuteQAccessibleWidgetV2(object, role);
}

//  QAccessibleWidgetV2::QAccessibleWidgetV2(QWidget *object,
//      QAccessible::Role role, const QString &name)
extern "C" Q_DECL_EXPORT
QAccessibleWidgetV2 *ritual_ZN19QAccessibleWidgetV2C1EP7QWidgetN11QAccessible4RoleERK7QString(
    QWidget *object,
    QAccessible::Role role,
    const QString *name) {
  return new CuteQAccessibleWidgetV2(object, role, *name);
}

//  QAccessibleWidgetV2::~QAccessibleWidgetV2()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibleWidgetV2D1Ev(QAccessibleWidgetV2 *self) {
  delete self;
}

//  void *QAccessibleWidgetV2::interface_cast(QAccessible::InterfaceType t)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QAccessibleWidgetV214interface_castEN11QAccessible13InterfaceTypeE(
    QAccessibleWidgetV2 *self,
    QAccessible::InterfaceType t) {
  return self->interface_cast(t);
}

//  QList<QAccessible::Attribute> QAccessibleWidgetV2::attributeKeys() const
extern "C" Q_DECL_EXPORT
QList<QAccessible::Attribute> *ritual_ZNK19QAccessibleWidgetV213attributeKeysEv(
    const QAccessibleWidgetV2 *self) {
  return new QList<QAccessible::Attribute>(self->attributeKeys());
}

//  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute key)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QAccessibleWidgetV214attributeValueEN11QAccessible9AttributeE(
    const QAccessibleWidgetV2 *self,
    QAccessible::Attribute key) {
  return new QVariant(self->attributeValue(key));
}

//  QAccessibleWidgetV2 as the QAccessibleAttributesInterface it is built on
extern "C" Q_DECL_EXPORT
QAccessibleAttributesInterface *ritual_cast_QAccessibleWidgetV2_QAccessibleAttributesInterface(
    QAccessibleWidgetV2 *self) {
  return static_cast<QAccessibleAttributesInterface *>(self);
}

//  a Python function taken by a CuteQAccessibleWidgetV2, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleWidgetV2(
    QAccessibleWidgetV2 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleWidgetV2 *>(self)->take(key, call);
}

//  void *QAccessibleWidgetV2::interface_cast(QAccessible::InterfaceType t)
extern "C" Q_DECL_EXPORT
void *ritual_own_ZN19QAccessibleWidgetV214interface_castEN11QAccessible13InterfaceTypeE(
    QAccessibleWidgetV2 *self,
    QAccessible::InterfaceType t) {
  return self->QAccessibleWidgetV2::interface_cast(t);
}

//  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute key)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK19QAccessibleWidgetV214attributeValueEN11QAccessible9AttributeE(
    const QAccessibleWidgetV2 *self,
    QAccessible::Attribute key) {
  return new QVariant(self->QAccessibleWidgetV2::attributeValue(key));
}

//  a QList<QAccessible::Attribute> a ritual of QAccessibleWidgetV2 gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAccessibleWidgetV2__QList_QAccessible_Attribute(
    QList<QAccessible::Attribute> *self) {
  delete self;
}

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
