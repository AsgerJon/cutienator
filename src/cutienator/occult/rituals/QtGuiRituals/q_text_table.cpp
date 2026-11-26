//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtexttable.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtexttable.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextcursor.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QTextTable that Python can take functions over in. Every QTextTable
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTextTableCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTextTableCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextTableCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextTableCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextTableCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextTableCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextTableCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTextTable : public QTextTable {
public:
  using QTextTable::QTextTable;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTextTableCall0 call = reinterpret_cast<CuteQTextTableCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTextTableCall1 call = reinterpret_cast<CuteQTextTableCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTextTableCall2 call = reinterpret_cast<CuteQTextTableCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTextTableCall3 call = reinterpret_cast<CuteQTextTableCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTextTableCall4 call = reinterpret_cast<CuteQTextTableCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTextTableCall5 call = reinterpret_cast<CuteQTextTableCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTextTableCall6 call = reinterpret_cast<CuteQTextTableCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTextTable::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QTextTable10metaObjectEv(
    const QTextTable *self) {
  return self->metaObject();
}

//  void *QTextTable::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QTextTable11qt_metacastEPKc(
    QTextTable *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QTextTable::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QTextTable11qt_metacallEN11QMetaObject4CallEiPPv(
    QTextTable *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QTextTable::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QTextTable2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTextTable::tr(s, c, n));
}

//  QTextTable::QTextTable(QTextDocument *doc)
extern "C" Q_DECL_EXPORT
QTextTable *ritual_ZN10QTextTableC1EP13QTextDocument(QTextDocument *doc) {
  return new CuteQTextTable(doc);
}

//  QTextTable::~QTextTable()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextTableD1Ev(QTextTable *self) {
  delete self;
}

//  void QTextTable::resize(int rows, int cols)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextTable6resizeEii(QTextTable *self, int rows, int cols) {
  self->resize(rows, cols);
}

//  void QTextTable::insertRows(int pos, int num)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextTable10insertRowsEii(
    QTextTable *self,
    int pos,
    int num) {
  self->insertRows(pos, num);
}

//  void QTextTable::insertColumns(int pos, int num)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextTable13insertColumnsEii(
    QTextTable *self,
    int pos,
    int num) {
  self->insertColumns(pos, num);
}

//  void QTextTable::appendRows(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextTable10appendRowsEi(QTextTable *self, int count) {
  self->appendRows(count);
}

//  void QTextTable::appendColumns(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextTable13appendColumnsEi(QTextTable *self, int count) {
  self->appendColumns(count);
}

//  void QTextTable::removeRows(int pos, int num)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextTable10removeRowsEii(
    QTextTable *self,
    int pos,
    int num) {
  self->removeRows(pos, num);
}

//  void QTextTable::removeColumns(int pos, int num)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextTable13removeColumnsEii(
    QTextTable *self,
    int pos,
    int num) {
  self->removeColumns(pos, num);
}

//  void QTextTable::mergeCells(int row, int col, int numRows, int numCols)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextTable10mergeCellsEiiii(
    QTextTable *self,
    int row,
    int col,
    int numRows,
    int numCols) {
  self->mergeCells(row, col, numRows, numCols);
}

//  void QTextTable::mergeCells(const QTextCursor &cursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextTable10mergeCellsERK11QTextCursor(
    QTextTable *self,
    const QTextCursor *cursor) {
  self->mergeCells(*cursor);
}

//  void QTextTable::splitCell(int row, int col, int numRows, int numCols)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextTable9splitCellEiiii(
    QTextTable *self,
    int row,
    int col,
    int numRows,
    int numCols) {
  self->splitCell(row, col, numRows, numCols);
}

//  int QTextTable::rows() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTextTable4rowsEv(const QTextTable *self) {
  return self->rows();
}

//  int QTextTable::columns() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTextTable7columnsEv(const QTextTable *self) {
  return self->columns();
}

//  QTextTableCell QTextTable::cellAt(int row, int col) const
extern "C" Q_DECL_EXPORT
QTextTableCell *ritual_ZNK10QTextTable6cellAtEii(
    const QTextTable *self,
    int row,
    int col) {
  return new QTextTableCell(self->cellAt(row, col));
}

//  QTextTableCell QTextTable::cellAt(int position) const
extern "C" Q_DECL_EXPORT
QTextTableCell *ritual_ZNK10QTextTable6cellAtEi(
    const QTextTable *self,
    int position) {
  return new QTextTableCell(self->cellAt(position));
}

//  QTextTableCell QTextTable::cellAt(const QTextCursor &c) const
extern "C" Q_DECL_EXPORT
QTextTableCell *ritual_ZNK10QTextTable6cellAtERK11QTextCursor(
    const QTextTable *self,
    const QTextCursor *c) {
  return new QTextTableCell(self->cellAt(*c));
}

//  QTextCursor QTextTable::rowStart(const QTextCursor &c) const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK10QTextTable8rowStartERK11QTextCursor(
    const QTextTable *self,
    const QTextCursor *c) {
  return new QTextCursor(self->rowStart(*c));
}

//  QTextCursor QTextTable::rowEnd(const QTextCursor &c) const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK10QTextTable6rowEndERK11QTextCursor(
    const QTextTable *self,
    const QTextCursor *c) {
  return new QTextCursor(self->rowEnd(*c));
}

//  void QTextTable::setFormat(const QTextTableFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextTable9setFormatERK16QTextTableFormat(
    QTextTable *self,
    const QTextTableFormat *format) {
  self->setFormat(*format);
}

//  QTextTableFormat QTextTable::format() const
extern "C" Q_DECL_EXPORT
QTextTableFormat *ritual_ZNK10QTextTable6formatEv(const QTextTable *self) {
  return new QTextTableFormat(self->format());
}

//  QTextTablePrivate *QTextTable::d_func()
extern "C" Q_DECL_EXPORT
QTextTablePrivate *ritual_ZN10QTextTable6d_funcEv(QTextTable *self) {
  return self->d_func();
}

//  const QTextTablePrivate *QTextTable::d_func() const
extern "C" Q_DECL_EXPORT
const QTextTablePrivate *ritual_ZNK10QTextTable6d_funcEv(
    const QTextTable *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQTextTable, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextTable(QTextTable *self, const char *key, void *call) {
  return static_cast<CuteQTextTable *>(self)->take(key, call);
}
