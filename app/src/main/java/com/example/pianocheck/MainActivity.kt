package com.example.pianocheck

import android.app.AlertDialog
import android.app.Dialog
import android.content.Context
import android.content.ContextParams
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
    fun onLoadSheet(view: View?){
        val builder: AlertDialog.Builder = AlertDialog.Builder(this)
        builder.setMessage("Loading Sheet...").setTitle("Load Recording")

        val dialog: AlertDialog = builder.create()
        dialog.show()
    }

    fun onLoadRecording(view: View?){
        val builder: AlertDialog.Builder = AlertDialog.Builder(this)
        builder.setMessage("Loading Recording...").setTitle("Load Recording")

        val dialog: AlertDialog = builder.create()
        dialog.show()
    }
    fun onPlay(view: View?){
        val builder: AlertDialog.Builder = AlertDialog.Builder(this)
        builder.setMessage("Checking your recording...").setTitle("Play")

        val dialog: AlertDialog = builder.create()
        dialog.show()
    }

}