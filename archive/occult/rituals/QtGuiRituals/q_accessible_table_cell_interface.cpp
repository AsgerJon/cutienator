//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QAccessibleTableCellInterface that Python can take functions over in. Every QAccessibleTableCellInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQAccessibleTableCellInterfaceCall0)(const void *, int *);
typedef int (*CuteQAccessibleTableCellInterfaceCall1)(const void *, int *);
typedef int (*CuteQAccessibleTableCellInterfaceCall2)(const void *, int *);
typedef int (*CuteQAccessibleTableCellInterfaceCall3)(const void *, int *);
typedef int (*CuteQAccessibleTableCellInterfaceCall4)(const void *, int *);
typedef void * (*CuteQAccessibleTableCellInterfaceCall5)(const void *, int *);
class CuteQAccessibleTableCellInterface : public QAccessibleTableCellInterface {
public:
  using QAccessibleTableCellInterface::QAccessibleTableCellInterface;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK29QAccessibleTableCellInterface10isSelectedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QAccessibleTableCellInterface11columnIndexEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QAccessibleTableCellInterface8rowIndexEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QAccessibleTableCellInterface12columnExtentEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QAccessibleTableCellInterface9rowExtentEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QAccessibleTableCellInterface5tableEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  bool QAccessibleTableCellInterface::isSelected() const
  bool isSelected() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleTableCellInterfaceCall0 call = reinterpret_cast<CuteQAccessibleTableCellInterfaceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QAccessibleTableCellInterface::columnIndex() const
  int columnIndex() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleTableCellInterfaceCall1 call = reinterpret_cast<CuteQAccessibleTableCellInterfaceCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QAccessibleTableCellInterface::rowIndex() const
  int rowIndex() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleTableCellInterfaceCall2 call = reinterpret_cast<CuteQAccessibleTableCellInterfaceCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QAccessibleTableCellInterface::columnExtent() const
  int columnExtent() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleTableCellInterfaceCall3 call = reinterpret_cast<CuteQAccessibleTableCellInterfaceCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QAccessibleTableCellInterface::rowExtent() const
  int rowExtent() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleTableCellInterfaceCall4 call = reinterpret_cast<CuteQAccessibleTableCellInterfaceCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QAccessibleInterface *QAccessibleTableCellInterface::table() const
  QAccessibleInterface *table() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleTableCellInterfaceCall5 call = reinterpret_cast<CuteQAccessibleTableCellInterfaceCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return {};
  }
};

//  QAccessibleTableCellInterface::~QAccessibleTableCellInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QAccessibleTableCellInterfaceD1Ev(
    QAccessibleTableCellInterface *self) {
  delete self;
}

//  bool QAccessibleTableCellInterface::isSelected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QAccessibleTableCellInterface10isSelectedEv(
    const QAccessibleTableCellInterface *self) {
  return self->isSelected();
}

//  QList<QAccessibleInterface *>
//      QAccessibleTableCellInterface::columnHeaderCells() const
extern "C" Q_DECL_EXPORT
QList<QAccessibleInterface *> *ritual_ZNK29QAccessibleTableCellInterface17columnHeaderCellsEv(
    const QAccessibleTableCellInterface *self) {
  return new QList<QAccessibleInterface *>(self->columnHeaderCells());
}

//  QList<QAccessibleInterface *>
//      QAccessibleTableCellInterface::rowHeaderCells() const
extern "C" Q_DECL_EXPORT
QList<QAccessibleInterface *> *ritual_ZNK29QAccessibleTableCellInterface14rowHeaderCellsEv(
    const QAccessibleTableCellInterface *self) {
  return new QList<QAccessibleInterface *>(self->rowHeaderCells());
}

//  int QAccessibleTableCellInterface::columnIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleTableCellInterface11columnIndexEv(
    const QAccessibleTableCellInterface *self) {
  return self->columnIndex();
}

//  int QAccessibleTableCellInterface::rowIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleTableCellInterface8rowIndexEv(
    const QAccessibleTableCellInterface *self) {
  return self->rowIndex();
}

//  int QAccessibleTableCellInterface::columnExtent() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleTableCellInterface12columnExtentEv(
    const QAccessibleTableCellInterface *self) {
  return self->columnExtent();
}

//  int QAccessibleTableCellInterface::rowExtent() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleTableCellInterface9rowExtentEv(
    const QAccessibleTableCellInterface *self) {
  return self->rowExtent();
}

//  QAccessibleInterface *QAccessibleTableCellInterface::table() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK29QAccessibleTableCellInterface5tableEv(
    const QAccessibleTableCellInterface *self) {
  return self->table();
}

//  a Python function taken by a CuteQAccessibleTableCellInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleTableCellInterface(
    QAccessibleTableCellInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleTableCellInterface *>(self)->take(key, call);
}
