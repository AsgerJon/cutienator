//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/container.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/container.h>
#include <cstring>

//  A QDesignerContainerExtension that Python can take functions over in. Every QDesignerContainerExtension
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQDesignerContainerExtensionCall0)(const void *, int *);
typedef void * (*CuteQDesignerContainerExtensionCall1)(const void *, int, int *);
typedef int (*CuteQDesignerContainerExtensionCall2)(const void *, int *);
typedef void (*CuteQDesignerContainerExtensionCall3)(const void *, int, int *);
typedef bool (*CuteQDesignerContainerExtensionCall4)(const void *, int *);
typedef void (*CuteQDesignerContainerExtensionCall5)(const void *, QWidget *, int *);
typedef void (*CuteQDesignerContainerExtensionCall6)(const void *, int, QWidget *, int *);
typedef bool (*CuteQDesignerContainerExtensionCall7)(const void *, int, int *);
typedef void (*CuteQDesignerContainerExtensionCall8)(const void *, int, int *);
class CuteQDesignerContainerExtension : public QDesignerContainerExtension {
public:
  using QDesignerContainerExtension::QDesignerContainerExtension;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK27QDesignerContainerExtension5countEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QDesignerContainerExtension6widgetEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QDesignerContainerExtension12currentIndexEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerContainerExtension15setCurrentIndexEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QDesignerContainerExtension12canAddWidgetEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerContainerExtension9addWidgetEP7QWidget")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerContainerExtension12insertWidgetEiP7QWidget")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QDesignerContainerExtension9canRemoveEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerContainerExtension6removeEi")) {
      taken[8] = call;
      return true;
    }
    return false;
  }

  //  int QDesignerContainerExtension::count() const
  int count() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerContainerExtensionCall0 call = reinterpret_cast<CuteQDesignerContainerExtensionCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QWidget *QDesignerContainerExtension::widget(int index) const
  QWidget *widget(int index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerContainerExtensionCall1 call = reinterpret_cast<CuteQDesignerContainerExtensionCall1>(taken[1]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  int QDesignerContainerExtension::currentIndex() const
  int currentIndex() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerContainerExtensionCall2 call = reinterpret_cast<CuteQDesignerContainerExtensionCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerContainerExtension::setCurrentIndex(int index)
  void setCurrentIndex(int index) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerContainerExtensionCall3 call = reinterpret_cast<CuteQDesignerContainerExtensionCall3>(taken[3]);
      call(this, index, &handled);
      if (handled) return;
    }
  }

  //  bool QDesignerContainerExtension::canAddWidget() const
  bool canAddWidget() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerContainerExtensionCall4 call = reinterpret_cast<CuteQDesignerContainerExtensionCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerContainerExtension::addWidget(QWidget *widget)
  void addWidget(QWidget *widget) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerContainerExtensionCall5 call = reinterpret_cast<CuteQDesignerContainerExtensionCall5>(taken[5]);
      call(this, widget, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerContainerExtension::insertWidget(int index, QWidget
  //      *widget)
  void insertWidget(int index, QWidget *widget) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerContainerExtensionCall6 call = reinterpret_cast<CuteQDesignerContainerExtensionCall6>(taken[6]);
      call(this, index, widget, &handled);
      if (handled) return;
    }
  }

  //  bool QDesignerContainerExtension::canRemove(int index) const
  bool canRemove(int index) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerContainerExtensionCall7 call = reinterpret_cast<CuteQDesignerContainerExtensionCall7>(taken[7]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerContainerExtension::remove(int index)
  void remove(int index) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerContainerExtensionCall8 call = reinterpret_cast<CuteQDesignerContainerExtensionCall8>(taken[8]);
      call(this, index, &handled);
      if (handled) return;
    }
  }
};

//  QDesignerContainerExtension::QDesignerContainerExtension()
extern "C" Q_DECL_EXPORT
QDesignerContainerExtension *ritual_ZN27QDesignerContainerExtensionC1Ev() {
  return new CuteQDesignerContainerExtension();
}

//  QDesignerContainerExtension::~QDesignerContainerExtension()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerContainerExtensionD1Ev(
    QDesignerContainerExtension *self) {
  delete self;
}

//  int QDesignerContainerExtension::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QDesignerContainerExtension5countEv(
    const QDesignerContainerExtension *self) {
  return self->count();
}

//  QWidget *QDesignerContainerExtension::widget(int index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK27QDesignerContainerExtension6widgetEi(
    const QDesignerContainerExtension *self,
    int index) {
  return self->widget(index);
}

//  int QDesignerContainerExtension::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QDesignerContainerExtension12currentIndexEv(
    const QDesignerContainerExtension *self) {
  return self->currentIndex();
}

//  void QDesignerContainerExtension::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerContainerExtension15setCurrentIndexEi(
    QDesignerContainerExtension *self,
    int index) {
  self->setCurrentIndex(index);
}

//  bool QDesignerContainerExtension::canAddWidget() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QDesignerContainerExtension12canAddWidgetEv(
    const QDesignerContainerExtension *self) {
  return self->canAddWidget();
}

//  void QDesignerContainerExtension::addWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerContainerExtension9addWidgetEP7QWidget(
    QDesignerContainerExtension *self,
    QWidget *widget) {
  self->addWidget(widget);
}

//  void QDesignerContainerExtension::insertWidget(int index, QWidget
//      *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerContainerExtension12insertWidgetEiP7QWidget(
    QDesignerContainerExtension *self,
    int index,
    QWidget *widget) {
  self->insertWidget(index, widget);
}

//  bool QDesignerContainerExtension::canRemove(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QDesignerContainerExtension9canRemoveEi(
    const QDesignerContainerExtension *self,
    int index) {
  return self->canRemove(index);
}

//  void QDesignerContainerExtension::remove(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerContainerExtension6removeEi(
    QDesignerContainerExtension *self,
    int index) {
  self->remove(index);
}

//  a Python function taken by a CuteQDesignerContainerExtension, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerContainerExtension(
    QDesignerContainerExtension *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerContainerExtension *>(self)->take(key, call);
}
