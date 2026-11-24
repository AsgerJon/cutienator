//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qaccessiblewidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(accessibility)
#include <QtWidgets/qaccessiblewidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtGui/qaccessible.h>
#include <QtGui/qcolor.h>
#include <cstring>

//  A QAccessibleWidgetV2 that Python can take functions over in. Every QAccessibleWidgetV2
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleWidgetV2Call0)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleWidgetV2Call1)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleWidgetV2Call2)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleWidgetV2Call3)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleWidgetV2Call4)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleWidgetV2Call5)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleWidgetV2Call6)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleWidgetV2Call7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleWidgetV2Call8)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleWidgetV2Call9)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleWidgetV2Call10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleWidgetV2Call11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleWidgetV2Call12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleWidgetV2Call13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleWidgetV2Call14)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleWidgetV2Call15)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleWidgetV2Call16)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleWidgetV2Call17)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleWidgetV2Call18)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleWidgetV2Call19)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleWidgetV2 : public QAccessibleWidgetV2 {
public:
  using QAccessibleWidgetV2::QAccessibleWidgetV2;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call0 call = reinterpret_cast<CuteQAccessibleWidgetV2Call0>(taken[0]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call1 call = reinterpret_cast<CuteQAccessibleWidgetV2Call1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call2 call = reinterpret_cast<CuteQAccessibleWidgetV2Call2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleWidget::childCount() const
  int childCount() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call3 call = reinterpret_cast<CuteQAccessibleWidgetV2Call3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call4 call = reinterpret_cast<CuteQAccessibleWidgetV2Call4>(taken[4]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::indexOfChild(child);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call5 call = reinterpret_cast<CuteQAccessibleWidgetV2Call5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call6 call = reinterpret_cast<CuteQAccessibleWidgetV2Call6>(taken[6]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call7 call = reinterpret_cast<CuteQAccessibleWidgetV2Call7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call8 call = reinterpret_cast<CuteQAccessibleWidgetV2Call8>(taken[8]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleWidget::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call9 call = reinterpret_cast<CuteQAccessibleWidgetV2Call9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call10 call = reinterpret_cast<CuteQAccessibleWidgetV2Call10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleWidget::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleWidget::state() const
  QAccessible::State state() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call11 call = reinterpret_cast<CuteQAccessibleWidgetV2Call11>(taken[11]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::state();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call12 call = reinterpret_cast<CuteQAccessibleWidgetV2Call12>(taken[12]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call13 call = reinterpret_cast<CuteQAccessibleWidgetV2Call13>(taken[13]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call14 call = reinterpret_cast<CuteQAccessibleWidgetV2Call14>(taken[14]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call15 call = reinterpret_cast<CuteQAccessibleWidgetV2Call15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call16 call = reinterpret_cast<CuteQAccessibleWidgetV2Call16>(taken[16]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call17 call = reinterpret_cast<CuteQAccessibleWidgetV2Call17>(taken[17]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleObject::childAt(x, y);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionName(const QString
  //      &name) const
  QString localizedActionName(const QString &name) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call18 call = reinterpret_cast<CuteQAccessibleWidgetV2Call18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleWidgetV2Call19 call = reinterpret_cast<CuteQAccessibleWidgetV2Call19>(taken[19]);
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

//  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute key)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK19QAccessibleWidgetV214attributeValueEN11QAccessible9AttributeE(
    const QAccessibleWidgetV2 *self,
    QAccessible::Attribute key) {
  return new QVariant(self->QAccessibleWidgetV2::attributeValue(key));
}

#endif  // QT_CONFIG(accessibility)
