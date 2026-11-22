//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <cstring>

//  A QAccessibleSelectionInterface that Python can take functions over in. Every QAccessibleSelectionInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQAccessibleSelectionInterfaceCall0)(const void *, int *);
typedef void * (*CuteQAccessibleSelectionInterfaceCall1)(const void *, int, int *);
typedef bool (*CuteQAccessibleSelectionInterfaceCall2)(const void *, QAccessibleInterface *, int *);
typedef bool (*CuteQAccessibleSelectionInterfaceCall3)(const void *, QAccessibleInterface *, int *);
typedef bool (*CuteQAccessibleSelectionInterfaceCall4)(const void *, QAccessibleInterface *, int *);
typedef bool (*CuteQAccessibleSelectionInterfaceCall5)(const void *, int *);
typedef bool (*CuteQAccessibleSelectionInterfaceCall6)(const void *, int *);
class CuteQAccessibleSelectionInterface : public QAccessibleSelectionInterface {
public:
  using QAccessibleSelectionInterface::QAccessibleSelectionInterface;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK29QAccessibleSelectionInterface17selectedItemCountEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QAccessibleSelectionInterface12selectedItemEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QAccessibleSelectionInterface10isSelectedEP20QAccessibleInterface")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAccessibleSelectionInterface6selectEP20QAccessibleInterface")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAccessibleSelectionInterface8unselectEP20QAccessibleInterface")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAccessibleSelectionInterface9selectAllEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAccessibleSelectionInterface5clearEv")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  int QAccessibleSelectionInterface::selectedItemCount() const
  int selectedItemCount() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleSelectionInterfaceCall0 call = reinterpret_cast<CuteQAccessibleSelectionInterfaceCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QAccessibleInterface *QAccessibleSelectionInterface::selectedItem(int
  //      selectionIndex) const
  QAccessibleInterface *selectedItem(int selectionIndex) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleSelectionInterfaceCall1 call = reinterpret_cast<CuteQAccessibleSelectionInterfaceCall1>(taken[1]);
      void * given = call(this, selectionIndex, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleSelectionInterface::selectedItem(selectionIndex);
  }

  //  bool QAccessibleSelectionInterface::isSelected(QAccessibleInterface
  //      *childItem) const
  bool isSelected(QAccessibleInterface *childItem) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleSelectionInterfaceCall2 call = reinterpret_cast<CuteQAccessibleSelectionInterfaceCall2>(taken[2]);
      bool given = call(this, childItem, &handled);
      if (handled) return given;
    }
    return QAccessibleSelectionInterface::isSelected(childItem);
  }

  //  bool QAccessibleSelectionInterface::select(QAccessibleInterface
  //      *childItem)
  bool select(QAccessibleInterface *childItem) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleSelectionInterfaceCall3 call = reinterpret_cast<CuteQAccessibleSelectionInterfaceCall3>(taken[3]);
      bool given = call(this, childItem, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QAccessibleSelectionInterface::unselect(QAccessibleInterface
  //      *childItem)
  bool unselect(QAccessibleInterface *childItem) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleSelectionInterfaceCall4 call = reinterpret_cast<CuteQAccessibleSelectionInterfaceCall4>(taken[4]);
      bool given = call(this, childItem, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QAccessibleSelectionInterface::selectAll()
  bool selectAll() override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleSelectionInterfaceCall5 call = reinterpret_cast<CuteQAccessibleSelectionInterfaceCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QAccessibleSelectionInterface::clear()
  bool clear() override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleSelectionInterfaceCall6 call = reinterpret_cast<CuteQAccessibleSelectionInterfaceCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QAccessibleSelectionInterface::~QAccessibleSelectionInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QAccessibleSelectionInterfaceD1Ev(
    QAccessibleSelectionInterface *self) {
  delete self;
}

//  int QAccessibleSelectionInterface::selectedItemCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleSelectionInterface17selectedItemCountEv(
    const QAccessibleSelectionInterface *self) {
  return self->selectedItemCount();
}

//  QAccessibleInterface *QAccessibleSelectionInterface::selectedItem(int
//      selectionIndex) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK29QAccessibleSelectionInterface12selectedItemEi(
    const QAccessibleSelectionInterface *self,
    int selectionIndex) {
  return self->selectedItem(selectionIndex);
}

//  bool QAccessibleSelectionInterface::isSelected(QAccessibleInterface
//      *childItem) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QAccessibleSelectionInterface10isSelectedEP20QAccessibleInterface(
    const QAccessibleSelectionInterface *self,
    QAccessibleInterface *childItem) {
  return self->isSelected(childItem);
}

//  bool QAccessibleSelectionInterface::select(QAccessibleInterface
//      *childItem)
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QAccessibleSelectionInterface6selectEP20QAccessibleInterface(
    QAccessibleSelectionInterface *self,
    QAccessibleInterface *childItem) {
  return self->select(childItem);
}

//  bool QAccessibleSelectionInterface::unselect(QAccessibleInterface
//      *childItem)
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QAccessibleSelectionInterface8unselectEP20QAccessibleInterface(
    QAccessibleSelectionInterface *self,
    QAccessibleInterface *childItem) {
  return self->unselect(childItem);
}

//  bool QAccessibleSelectionInterface::selectAll()
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QAccessibleSelectionInterface9selectAllEv(
    QAccessibleSelectionInterface *self) {
  return self->selectAll();
}

//  bool QAccessibleSelectionInterface::clear()
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QAccessibleSelectionInterface5clearEv(
    QAccessibleSelectionInterface *self) {
  return self->clear();
}

//  a Python function taken by a CuteQAccessibleSelectionInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleSelectionInterface(
    QAccessibleSelectionInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleSelectionInterface *>(self)->take(key, call);
}

//  QAccessibleInterface *QAccessibleSelectionInterface::selectedItem(int
//      selectionIndex) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK29QAccessibleSelectionInterface12selectedItemEi(
    const QAccessibleSelectionInterface *self,
    int selectionIndex) {
  return self->QAccessibleSelectionInterface::selectedItem(selectionIndex);
}

//  bool QAccessibleSelectionInterface::isSelected(QAccessibleInterface
//      *childItem) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK29QAccessibleSelectionInterface10isSelectedEP20QAccessibleInterface(
    const QAccessibleSelectionInterface *self,
    QAccessibleInterface *childItem) {
  return self->QAccessibleSelectionInterface::isSelected(childItem);
}
