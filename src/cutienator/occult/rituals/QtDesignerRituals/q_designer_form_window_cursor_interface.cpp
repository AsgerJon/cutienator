//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractformwindowcursor.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDesigner/abstractformwindowcursor.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A QDesignerFormWindowCursorInterface that Python can take functions over in. Every QDesignerFormWindowCursorInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDesignerFormWindowCursorInterfaceCall0)(const void *, int *);
typedef bool (*CuteQDesignerFormWindowCursorInterfaceCall1)(const void *, int, int, int *);
typedef int (*CuteQDesignerFormWindowCursorInterfaceCall2)(const void *, int *);
typedef void (*CuteQDesignerFormWindowCursorInterfaceCall3)(const void *, int, int, int *);
typedef void * (*CuteQDesignerFormWindowCursorInterfaceCall4)(const void *, int *);
typedef int (*CuteQDesignerFormWindowCursorInterfaceCall5)(const void *, int *);
typedef void * (*CuteQDesignerFormWindowCursorInterfaceCall6)(const void *, int, int *);
typedef bool (*CuteQDesignerFormWindowCursorInterfaceCall7)(const void *, int *);
typedef int (*CuteQDesignerFormWindowCursorInterfaceCall8)(const void *, int *);
typedef void * (*CuteQDesignerFormWindowCursorInterfaceCall9)(const void *, int, int *);
typedef void (*CuteQDesignerFormWindowCursorInterfaceCall10)(const void *, const QString *, const QVariant *, int *);
typedef void (*CuteQDesignerFormWindowCursorInterfaceCall11)(const void *, QWidget *, const QString *, const QVariant *, int *);
typedef void (*CuteQDesignerFormWindowCursorInterfaceCall12)(const void *, QWidget *, const QString *, int *);
class CuteQDesignerFormWindowCursorInterface : public QDesignerFormWindowCursorInterface {
public:
  using QDesignerFormWindowCursorInterface::QDesignerFormWindowCursorInterface;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK34QDesignerFormWindowCursorInterface10formWindowEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDesignerFormWindowCursorInterface12movePositionENS_13MoveOperationENS_8MoveModeE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerFormWindowCursorInterface8positionEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDesignerFormWindowCursorInterface11setPositionEiNS_8MoveModeE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerFormWindowCursorInterface7currentEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerFormWindowCursorInterface11widgetCountEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerFormWindowCursorInterface6widgetEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerFormWindowCursorInterface12hasSelectionEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerFormWindowCursorInterface19selectedWidgetCountEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerFormWindowCursorInterface14selectedWidgetEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDesignerFormWindowCursorInterface11setPropertyERK7QStringRK8QVariant")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDesignerFormWindowCursorInterface17setWidgetPropertyEP7QWidgetRK7QStringRK8QVariant")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDesignerFormWindowCursorInterface19resetWidgetPropertyEP7QWidgetRK7QString")) {
      taken[12] = call;
      return true;
    }
    return false;
  }

  //  QDesignerFormWindowInterface
  //      *QDesignerFormWindowCursorInterface::formWindow() const
  QDesignerFormWindowInterface *formWindow() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerFormWindowCursorInterfaceCall0 call = reinterpret_cast<CuteQDesignerFormWindowCursorInterfaceCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormWindowInterface *>(given);
    }
    return {};
  }

  //  bool QDesignerFormWindowCursorInterface::movePosition(MoveOperation
  //      op, MoveMode mode)
  bool movePosition(
      QDesignerFormWindowCursorInterface::MoveOperation op,
      QDesignerFormWindowCursorInterface::MoveMode mode) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerFormWindowCursorInterfaceCall1 call = reinterpret_cast<CuteQDesignerFormWindowCursorInterfaceCall1>(taken[1]);
      bool given = call(this, static_cast<int>(op), static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerFormWindowCursorInterface::position() const
  int position() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerFormWindowCursorInterfaceCall2 call = reinterpret_cast<CuteQDesignerFormWindowCursorInterfaceCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerFormWindowCursorInterface::setPosition(int pos,
  //      MoveMode mode)
  void setPosition(
      int pos,
      QDesignerFormWindowCursorInterface::MoveMode mode) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerFormWindowCursorInterfaceCall3 call = reinterpret_cast<CuteQDesignerFormWindowCursorInterfaceCall3>(taken[3]);
      call(this, pos, static_cast<int>(mode), &handled);
      if (handled) return;
    }
  }

  //  QWidget *QDesignerFormWindowCursorInterface::current() const
  QWidget *current() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerFormWindowCursorInterfaceCall4 call = reinterpret_cast<CuteQDesignerFormWindowCursorInterfaceCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  int QDesignerFormWindowCursorInterface::widgetCount() const
  int widgetCount() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerFormWindowCursorInterfaceCall5 call = reinterpret_cast<CuteQDesignerFormWindowCursorInterfaceCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QWidget *QDesignerFormWindowCursorInterface::widget(int index) const
  QWidget *widget(int index) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerFormWindowCursorInterfaceCall6 call = reinterpret_cast<CuteQDesignerFormWindowCursorInterfaceCall6>(taken[6]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  bool QDesignerFormWindowCursorInterface::hasSelection() const
  bool hasSelection() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerFormWindowCursorInterfaceCall7 call = reinterpret_cast<CuteQDesignerFormWindowCursorInterfaceCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerFormWindowCursorInterface::selectedWidgetCount() const
  int selectedWidgetCount() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerFormWindowCursorInterfaceCall8 call = reinterpret_cast<CuteQDesignerFormWindowCursorInterfaceCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QWidget *QDesignerFormWindowCursorInterface::selectedWidget(int
  //      index) const
  QWidget *selectedWidget(int index) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerFormWindowCursorInterfaceCall9 call = reinterpret_cast<CuteQDesignerFormWindowCursorInterfaceCall9>(taken[9]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  void QDesignerFormWindowCursorInterface::setProperty(const QString
  //      &name, const QVariant &value)
  void setProperty(const QString &name, const QVariant &value) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerFormWindowCursorInterfaceCall10 call = reinterpret_cast<CuteQDesignerFormWindowCursorInterfaceCall10>(taken[10]);
      call(this, &name, &value, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowCursorInterface::setWidgetProperty(QWidget
  //      *widget, const QString &name, const QVariant &value)
  void setWidgetProperty(
      QWidget *widget,
      const QString &name,
      const QVariant &value) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerFormWindowCursorInterfaceCall11 call = reinterpret_cast<CuteQDesignerFormWindowCursorInterfaceCall11>(taken[11]);
      call(this, widget, &name, &value, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowCursorInterface::resetWidgetProperty(QWidget
  //      *widget, const QString &name)
  void resetWidgetProperty(QWidget *widget, const QString &name) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDesignerFormWindowCursorInterfaceCall12 call = reinterpret_cast<CuteQDesignerFormWindowCursorInterfaceCall12>(taken[12]);
      call(this, widget, &name, &handled);
      if (handled) return;
    }
  }
};

//  QDesignerFormWindowCursorInterface::QDesignerFormWindowCursorInterface()
extern "C" Q_DECL_EXPORT
QDesignerFormWindowCursorInterface *ritual_ZN34QDesignerFormWindowCursorInterfaceC1Ev() {
  return new CuteQDesignerFormWindowCursorInterface();
}

//  QDesignerFormWindowCursorInterface::~QDesignerFormWindowCursorInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDesignerFormWindowCursorInterfaceD1Ev(
    QDesignerFormWindowCursorInterface *self) {
  delete self;
}

//  QDesignerFormWindowInterface
//      *QDesignerFormWindowCursorInterface::formWindow() const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface *ritual_ZNK34QDesignerFormWindowCursorInterface10formWindowEv(
    const QDesignerFormWindowCursorInterface *self) {
  return self->formWindow();
}

//  bool QDesignerFormWindowCursorInterface::movePosition(MoveOperation op,
//      MoveMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN34QDesignerFormWindowCursorInterface12movePositionENS_13MoveOperationENS_8MoveModeE(
    QDesignerFormWindowCursorInterface *self,
    QDesignerFormWindowCursorInterface::MoveOperation op,
    QDesignerFormWindowCursorInterface::MoveMode mode) {
  return self->movePosition(op, mode);
}

//  int QDesignerFormWindowCursorInterface::position() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK34QDesignerFormWindowCursorInterface8positionEv(
    const QDesignerFormWindowCursorInterface *self) {
  return self->position();
}

//  void QDesignerFormWindowCursorInterface::setPosition(int pos, MoveMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDesignerFormWindowCursorInterface11setPositionEiNS_8MoveModeE(
    QDesignerFormWindowCursorInterface *self,
    int pos,
    QDesignerFormWindowCursorInterface::MoveMode mode) {
  self->setPosition(pos, mode);
}

//  QWidget *QDesignerFormWindowCursorInterface::current() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK34QDesignerFormWindowCursorInterface7currentEv(
    const QDesignerFormWindowCursorInterface *self) {
  return self->current();
}

//  int QDesignerFormWindowCursorInterface::widgetCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK34QDesignerFormWindowCursorInterface11widgetCountEv(
    const QDesignerFormWindowCursorInterface *self) {
  return self->widgetCount();
}

//  QWidget *QDesignerFormWindowCursorInterface::widget(int index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK34QDesignerFormWindowCursorInterface6widgetEi(
    const QDesignerFormWindowCursorInterface *self,
    int index) {
  return self->widget(index);
}

//  bool QDesignerFormWindowCursorInterface::hasSelection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK34QDesignerFormWindowCursorInterface12hasSelectionEv(
    const QDesignerFormWindowCursorInterface *self) {
  return self->hasSelection();
}

//  int QDesignerFormWindowCursorInterface::selectedWidgetCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK34QDesignerFormWindowCursorInterface19selectedWidgetCountEv(
    const QDesignerFormWindowCursorInterface *self) {
  return self->selectedWidgetCount();
}

//  QWidget *QDesignerFormWindowCursorInterface::selectedWidget(int index)
//      const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK34QDesignerFormWindowCursorInterface14selectedWidgetEi(
    const QDesignerFormWindowCursorInterface *self,
    int index) {
  return self->selectedWidget(index);
}

//  void QDesignerFormWindowCursorInterface::setProperty(const QString &name,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDesignerFormWindowCursorInterface11setPropertyERK7QStringRK8QVariant(
    QDesignerFormWindowCursorInterface *self,
    const QString *name,
    const QVariant *value) {
  self->setProperty(*name, *value);
}

//  void QDesignerFormWindowCursorInterface::setWidgetProperty(QWidget
//      *widget, const QString &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDesignerFormWindowCursorInterface17setWidgetPropertyEP7QWidgetRK7QStringRK8QVariant(
    QDesignerFormWindowCursorInterface *self,
    QWidget *widget,
    const QString *name,
    const QVariant *value) {
  self->setWidgetProperty(widget, *name, *value);
}

//  void QDesignerFormWindowCursorInterface::resetWidgetProperty(QWidget
//      *widget, const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDesignerFormWindowCursorInterface19resetWidgetPropertyEP7QWidgetRK7QString(
    QDesignerFormWindowCursorInterface *self,
    QWidget *widget,
    const QString *name) {
  self->resetWidgetProperty(widget, *name);
}

//  bool QDesignerFormWindowCursorInterface::isWidgetSelected(QWidget
//      *widget) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK34QDesignerFormWindowCursorInterface16isWidgetSelectedEP7QWidget(
    const QDesignerFormWindowCursorInterface *self,
    QWidget *widget) {
  return self->isWidgetSelected(widget);
}

//  a Python function taken by a CuteQDesignerFormWindowCursorInterface, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerFormWindowCursorInterface(
    QDesignerFormWindowCursorInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerFormWindowCursorInterface *>(self)->take(key, call);
}
