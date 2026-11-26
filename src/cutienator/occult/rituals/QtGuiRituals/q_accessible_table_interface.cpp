//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>

//  A QAccessibleTableInterface that Python can take functions over in. Every QAccessibleTableInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTableInterfaceCall0)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTableInterfaceCall1)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTableInterfaceCall2)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleTableInterfaceCall3)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleTableInterfaceCall4)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleTableInterfaceCall5)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleTableInterfaceCall6)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleTableInterfaceCall7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleTableInterfaceCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleTableInterfaceCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleTableInterfaceCall10)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleTableInterfaceCall11)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleTableInterfaceCall12)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleTableInterfaceCall13)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleTableInterfaceCall14)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleTableInterfaceCall15)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleTableInterfaceCall16)(const void *, QAccessibleTableModelChangeEvent *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleTableInterface : public QAccessibleTableInterface {
public:
  using QAccessibleTableInterface::QAccessibleTableInterface;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface7captionEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface7summaryEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface6cellAtEii")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface17selectedCellCountEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface17columnDescriptionEi")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface14rowDescriptionEi")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface19selectedColumnCountEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface16selectedRowCountEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface11columnCountEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface8rowCountEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface16isColumnSelectedEi")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface13isRowSelectedEi")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN25QAccessibleTableInterface9selectRowEi")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN25QAccessibleTableInterface12selectColumnEi")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN25QAccessibleTableInterface11unselectRowEi")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN25QAccessibleTableInterface14unselectColumnEi")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN25QAccessibleTableInterface11modelChangeEP32QAccessibleTableModelChangeEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleTableInterface::caption() const
  QAccessibleInterface *caption() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleTableInterfaceCall0 call = reinterpret_cast<CuteQAccessibleTableInterfaceCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleTableInterface::summary() const
  QAccessibleInterface *summary() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleTableInterfaceCall1 call = reinterpret_cast<CuteQAccessibleTableInterfaceCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleTableInterface::cellAt(int row, int
  //      column) const
  QAccessibleInterface *cellAt(int row, int column) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleTableInterfaceCall2 call = reinterpret_cast<CuteQAccessibleTableInterfaceCall2>(taken[2]);
      void * given = call(this, row, column, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleTableInterface::selectedCellCount() const
  int selectedCellCount() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleTableInterfaceCall3 call = reinterpret_cast<CuteQAccessibleTableInterfaceCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleTableInterface::columnDescription(int column)
  //      const
  QString columnDescription(int column) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleTableInterfaceCall4 call = reinterpret_cast<CuteQAccessibleTableInterfaceCall4>(taken[4]);
      QString * given = call(this, column, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleTableInterface::rowDescription(int row) const
  QString rowDescription(int row) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleTableInterfaceCall5 call = reinterpret_cast<CuteQAccessibleTableInterfaceCall5>(taken[5]);
      QString * given = call(this, row, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleTableInterface::selectedColumnCount() const
  int selectedColumnCount() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleTableInterfaceCall6 call = reinterpret_cast<CuteQAccessibleTableInterfaceCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleTableInterface::selectedRowCount() const
  int selectedRowCount() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleTableInterfaceCall7 call = reinterpret_cast<CuteQAccessibleTableInterfaceCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleTableInterface::columnCount() const
  int columnCount() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleTableInterfaceCall8 call = reinterpret_cast<CuteQAccessibleTableInterfaceCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleTableInterface::rowCount() const
  int rowCount() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleTableInterfaceCall9 call = reinterpret_cast<CuteQAccessibleTableInterfaceCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleTableInterface::isColumnSelected(int column) const
  bool isColumnSelected(int column) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleTableInterfaceCall10 call = reinterpret_cast<CuteQAccessibleTableInterfaceCall10>(taken[10]);
      bool given = call(this, column, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleTableInterface::isRowSelected(int row) const
  bool isRowSelected(int row) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleTableInterfaceCall11 call = reinterpret_cast<CuteQAccessibleTableInterfaceCall11>(taken[11]);
      bool given = call(this, row, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleTableInterface::selectRow(int row)
  bool selectRow(int row) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleTableInterfaceCall12 call = reinterpret_cast<CuteQAccessibleTableInterfaceCall12>(taken[12]);
      bool given = call(this, row, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleTableInterface::selectColumn(int column)
  bool selectColumn(int column) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleTableInterfaceCall13 call = reinterpret_cast<CuteQAccessibleTableInterfaceCall13>(taken[13]);
      bool given = call(this, column, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleTableInterface::unselectRow(int row)
  bool unselectRow(int row) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleTableInterfaceCall14 call = reinterpret_cast<CuteQAccessibleTableInterfaceCall14>(taken[14]);
      bool given = call(this, row, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleTableInterface::unselectColumn(int column)
  bool unselectColumn(int column) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleTableInterfaceCall15 call = reinterpret_cast<CuteQAccessibleTableInterfaceCall15>(taken[15]);
      bool given = call(this, column, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleTableInterface::modelChange(QAccessibleTableModelChan
  //      geEvent *event)
  void modelChange(QAccessibleTableModelChangeEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleTableInterfaceCall16 call = reinterpret_cast<CuteQAccessibleTableInterfaceCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(accessibility)
};

//  QAccessibleTableInterface::~QAccessibleTableInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAccessibleTableInterfaceD1Ev(
    QAccessibleTableInterface *self) {
  delete self;
}

//  QAccessibleInterface *QAccessibleTableInterface::caption() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK25QAccessibleTableInterface7captionEv(
    const QAccessibleTableInterface *self) {
  return self->caption();
}

//  QAccessibleInterface *QAccessibleTableInterface::summary() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK25QAccessibleTableInterface7summaryEv(
    const QAccessibleTableInterface *self) {
  return self->summary();
}

//  QAccessibleInterface *QAccessibleTableInterface::cellAt(int row, int
//      column) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK25QAccessibleTableInterface6cellAtEii(
    const QAccessibleTableInterface *self,
    int row,
    int column) {
  return self->cellAt(row, column);
}

//  int QAccessibleTableInterface::selectedCellCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QAccessibleTableInterface17selectedCellCountEv(
    const QAccessibleTableInterface *self) {
  return self->selectedCellCount();
}

//  QList<QAccessibleInterface *> QAccessibleTableInterface::selectedCells()
//      const
extern "C" Q_DECL_EXPORT
QList<QAccessibleInterface *> *ritual_ZNK25QAccessibleTableInterface13selectedCellsEv(
    const QAccessibleTableInterface *self) {
  return new QList<QAccessibleInterface *>(self->selectedCells());
}

//  QString QAccessibleTableInterface::columnDescription(int column) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QAccessibleTableInterface17columnDescriptionEi(
    const QAccessibleTableInterface *self,
    int column) {
  return new QString(self->columnDescription(column));
}

//  QString QAccessibleTableInterface::rowDescription(int row) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QAccessibleTableInterface14rowDescriptionEi(
    const QAccessibleTableInterface *self,
    int row) {
  return new QString(self->rowDescription(row));
}

//  int QAccessibleTableInterface::selectedColumnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QAccessibleTableInterface19selectedColumnCountEv(
    const QAccessibleTableInterface *self) {
  return self->selectedColumnCount();
}

//  int QAccessibleTableInterface::selectedRowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QAccessibleTableInterface16selectedRowCountEv(
    const QAccessibleTableInterface *self) {
  return self->selectedRowCount();
}

//  int QAccessibleTableInterface::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QAccessibleTableInterface11columnCountEv(
    const QAccessibleTableInterface *self) {
  return self->columnCount();
}

//  int QAccessibleTableInterface::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QAccessibleTableInterface8rowCountEv(
    const QAccessibleTableInterface *self) {
  return self->rowCount();
}

//  QList<int> QAccessibleTableInterface::selectedColumns() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK25QAccessibleTableInterface15selectedColumnsEv(
    const QAccessibleTableInterface *self) {
  return new QList<int>(self->selectedColumns());
}

//  QList<int> QAccessibleTableInterface::selectedRows() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK25QAccessibleTableInterface12selectedRowsEv(
    const QAccessibleTableInterface *self) {
  return new QList<int>(self->selectedRows());
}

//  bool QAccessibleTableInterface::isColumnSelected(int column) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QAccessibleTableInterface16isColumnSelectedEi(
    const QAccessibleTableInterface *self,
    int column) {
  return self->isColumnSelected(column);
}

//  bool QAccessibleTableInterface::isRowSelected(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QAccessibleTableInterface13isRowSelectedEi(
    const QAccessibleTableInterface *self,
    int row) {
  return self->isRowSelected(row);
}

//  bool QAccessibleTableInterface::selectRow(int row)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAccessibleTableInterface9selectRowEi(
    QAccessibleTableInterface *self,
    int row) {
  return self->selectRow(row);
}

//  bool QAccessibleTableInterface::selectColumn(int column)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAccessibleTableInterface12selectColumnEi(
    QAccessibleTableInterface *self,
    int column) {
  return self->selectColumn(column);
}

//  bool QAccessibleTableInterface::unselectRow(int row)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAccessibleTableInterface11unselectRowEi(
    QAccessibleTableInterface *self,
    int row) {
  return self->unselectRow(row);
}

//  bool QAccessibleTableInterface::unselectColumn(int column)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAccessibleTableInterface14unselectColumnEi(
    QAccessibleTableInterface *self,
    int column) {
  return self->unselectColumn(column);
}

//  void
//      QAccessibleTableInterface::modelChange(QAccessibleTableModelChangeEve
//      nt *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAccessibleTableInterface11modelChangeEP32QAccessibleTableModelChangeEvent(
    QAccessibleTableInterface *self,
    QAccessibleTableModelChangeEvent *event) {
  self->modelChange(event);
}

//  a Python function taken by a CuteQAccessibleTableInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleTableInterface(
    QAccessibleTableInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleTableInterface *>(self)->take(key, call);
}

//  a QList<int> a ritual of QAccessibleTableInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAccessibleTableInterface__QList_int(QList<int> *self) {
  delete self;
}

#endif  // QT_CONFIG(accessibility)
